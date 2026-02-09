#!/usr/bin/env python3
"""Split runtime-associated blocks into per-plugin catalogs and render Markdown."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any, Dict, List


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build per-plugin runtime block catalogs.")
    parser.add_argument("--runtime-json", required=True, help="Runtime associated JSON path")
    parser.add_argument("--wp-version", required=True, help="WordPress version, e.g. 6.9.1")
    parser.add_argument("--out-dir", help="Docs output dir")
    parser.add_argument("--artifacts-dir", help="Artifacts output dir")
    parser.add_argument("--plugins-root", help="Path to wp-content/plugins for version lookup")
    return parser.parse_args()


def normalize_block(block: Dict[str, Any], plugin: str) -> Dict[str, Any]:
    normalized = dict(block)
    if "derived" not in normalized:
        normalized["derived"] = {"isDynamic": bool(normalized.get("isDynamic"))}
    normalized["origin"] = "plugin"
    normalized["originName"] = plugin
    return normalized


def extract_plugin_version(plugin_dir: Path) -> str:
    if not plugin_dir.exists():
        return ""
    candidates = list(plugin_dir.glob("*.php"))
    for path in candidates:
        try:
            head = path.read_text(encoding="utf-8", errors="ignore")[:8192]
        except Exception:
            continue
        if "Plugin Name" not in head:
            continue
        for line in head.splitlines():
            cleaned = line.strip().lstrip("*").strip()
            if cleaned.lower().startswith("version:"):
                return cleaned.split(":", 1)[1].strip()
    # Fallback: themes or non-plugin headers sometimes store versions in style.css or README.txt
    for filename in ("style.css", "README.txt", "readme.txt"):
        path = plugin_dir / filename
        if not path.exists():
            continue
        try:
            head = path.read_text(encoding="utf-8", errors="ignore")[:8192]
        except Exception:
            continue
        for line in head.splitlines():
            cleaned = line.strip().lstrip("*").strip()
            if cleaned.lower().startswith("version:"):
                return cleaned.split(":", 1)[1].strip()
    return ""


def main() -> None:
    args = parse_args()
    runtime_path = Path(args.runtime_json).expanduser().resolve()
    repo_root = Path(__file__).resolve().parents[1]
    out_dir = Path(args.out_dir or (repo_root / "docs")).expanduser().resolve()
    artifacts_dir = Path(args.artifacts_dir or (repo_root / "artifacts")).expanduser().resolve()
    plugins_root = Path(args.plugins_root).expanduser().resolve() if args.plugins_root else None

    payload = json.loads(runtime_path.read_text(encoding="utf-8"))
    blocks: List[Dict[str, Any]] = payload.get("blocks", [])

    by_plugin: Dict[str, List[Dict[str, Any]]] = {}
    for block in blocks:
        plugins = block.get("originPlugins") or []
        for plugin in plugins:
            by_plugin.setdefault(plugin, []).append(normalize_block(block, plugin))

    for plugin, plugin_blocks in sorted(by_plugin.items()):
        plugin_version = (
            extract_plugin_version(plugins_root / plugin) if plugins_root else ""
        )
        version_suffix = f"-{plugin_version}" if plugin_version else ""
        out_json = artifacts_dir / f"wp-{args.wp_version}-{plugin}{version_suffix}-blocks.json"
        out_md = out_dir / f"{plugin}{version_suffix}-blocks.md"

        out_json.parent.mkdir(parents=True, exist_ok=True)
        out_md.parent.mkdir(parents=True, exist_ok=True)

        out_payload = {
            "wordpressVersion": args.wp_version,
            "pluginSlug": plugin,
            "pluginVersion": plugin_version,
            "generated_at_utc": payload.get("generated_at_utc"),
            "blocks": plugin_blocks,
        }
        out_json.write_text(
            json.dumps(out_payload, indent=2, sort_keys=True), encoding="utf-8"
        )

        subprocess.run(
            [
                "python3",
                str(Path(__file__).resolve().parents[1] / "scripts" / "render_blocks_md.py"),
                "--in-json",
                str(out_json),
                "--out-md",
                str(out_md),
            ],
            check=True,
        )

        # No latest copy; files are versioned in docs root.


if __name__ == "__main__":
    main()
