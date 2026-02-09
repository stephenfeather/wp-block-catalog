#!/usr/bin/env python3
"""Associate runtime-registered blocks with plugins by scanning plugin sources."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Set


BLOCK_NAME_RE = re.compile(r"[a-z0-9-]+/[a-z0-9-]+")
SCAN_EXTS = {".php", ".js", ".jsx", ".ts", ".tsx", ".json"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Associate runtime blocks with plugin sources.")
    parser.add_argument("--runtime-json", required=True, help="Path to runtime blocks JSON")
    parser.add_argument("--plugins-root", required=True, help="Path to wp-content/plugins")
    parser.add_argument("--out-json", required=True, help="Output JSON path")
    return parser.parse_args()


def load_runtime_blocks(path: Path) -> List[Dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload.get("blocks", [])


def scan_plugin_for_blocks(plugin_dir: Path, block_names: Set[str]) -> Set[str]:
    hits: Set[str] = set()
    for file_path in plugin_dir.rglob("*"):
        if not file_path.is_file():
            continue
        if file_path.suffix.lower() not in SCAN_EXTS:
            continue
        try:
            content = file_path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for match in BLOCK_NAME_RE.findall(content):
            if match in block_names:
                hits.add(match)
    return hits


def main() -> None:
    args = parse_args()
    runtime_path = Path(args.runtime_json).expanduser().resolve()
    plugins_root = Path(args.plugins_root).expanduser().resolve()
    out_path = Path(args.out_json).expanduser().resolve()

    blocks = load_runtime_blocks(runtime_path)
    block_names = {b.get("name") for b in blocks if b.get("name")}

    plugin_dirs = [p for p in plugins_root.iterdir() if p.is_dir()]
    plugin_slugs = {p.name for p in plugin_dirs}

    associations: Dict[str, Set[str]] = {name: set() for name in block_names}

    # Heuristic: prefix match (e.g. woocommerce/* -> woocommerce)
    for name in block_names:
        if not name or "/" not in name:
            continue
        prefix = name.split("/", 1)[0]
        if prefix in plugin_slugs:
            associations[name].add(prefix)

    # Scan plugin sources for explicit mentions.
    for plugin_dir in plugin_dirs:
        hits = scan_plugin_for_blocks(plugin_dir, block_names)
        for block_name in hits:
            associations[block_name].add(plugin_dir.name)

    enriched_blocks = []
    for block in blocks:
        name = block.get("name")
        origin_plugins = sorted(associations.get(name, set()))
        block["originPlugins"] = origin_plugins
        enriched_blocks.append(block)

    payload = {
        "generated_at_utc": json.loads(runtime_path.read_text(encoding="utf-8")).get(
            "generated_at_utc"
        ),
        "count": len(enriched_blocks),
        "blocks": enriched_blocks,
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


if __name__ == "__main__":
    main()
