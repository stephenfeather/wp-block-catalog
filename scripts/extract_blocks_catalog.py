#!/usr/bin/env python3
"""Extract block metadata from a WordPress source tree.

Outputs a normalized JSON catalog (and optional CSV summary) for core and custom blocks.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


@dataclass
class SourceRoot:
    label: str
    path: Path


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def safe_read_json(path: Path) -> Optional[Dict[str, Any]]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def find_block_jsons(roots: Iterable[SourceRoot]) -> List[Tuple[SourceRoot, Path]]:
    matches: List[Tuple[SourceRoot, Path]] = []
    for root in roots:
        if not root.path.exists():
            continue
        for block_json in root.path.rglob("block.json"):
            matches.append((root, block_json))
    return matches


def infer_origin(block_json: Path, wp_root: Path) -> Tuple[str, Optional[str]]:
    """Infer origin (core/plugin/theme/custom) and origin name when possible."""
    try:
        rel = block_json.relative_to(wp_root)
    except Exception:
        return ("external", None)

    parts = rel.parts
    if len(parts) >= 2 and parts[0] == "wp-includes" and parts[1] == "blocks":
        return ("core", None)
    if len(parts) >= 3 and parts[0] == "wp-content" and parts[1] == "plugins":
        return ("plugin", parts[2])
    if len(parts) >= 3 and parts[0] == "wp-content" and parts[1] == "mu-plugins":
        return ("mu-plugin", parts[2])
    if len(parts) >= 3 and parts[0] == "wp-content" and parts[1] == "themes":
        return ("theme", parts[2])
    return ("custom", None)


def bool_from(value: Any) -> bool:
    return bool(value)


def build_entry(
    data: Dict[str, Any],
    block_json: Path,
    wp_root: Path,
    source_root: SourceRoot,
) -> Dict[str, Any]:
    block_dir = block_json.parent
    origin, origin_name = infer_origin(block_json, wp_root)

    has_render_php = (block_dir / "render.php").exists()
    has_index_php = (block_dir / "index.php").exists()
    has_view_js = (block_dir / "view.js").exists() or (block_dir / "view.asset.php").exists()

    render_prop = data.get("render")
    is_dynamic = bool_from(render_prop) or has_render_php

    try:
        rel_block_json = str(block_json.relative_to(wp_root))
    except Exception:
        rel_block_json = str(block_json)

    entry = {
        "name": data.get("name"),
        "title": data.get("title"),
        "category": data.get("category"),
        "keywords": data.get("keywords", []),
        "apiVersion": data.get("apiVersion"),
        "attributes": data.get("attributes", {}),
        "supports": data.get("supports", {}),
        "usesContext": data.get("usesContext", []),
        "providesContext": data.get("providesContext", {}),
        "render": render_prop,
        "origin": origin,
        "originName": origin_name,
        "sourceRoot": source_root.label,
        "filePaths": {
            "blockJson": rel_block_json,
            "hasRenderPhp": has_render_php,
            "hasIndexPhp": has_index_php,
            "hasViewJs": has_view_js,
        },
        "derived": {
            "isDynamic": is_dynamic,
        },
    }

    return entry


def normalize_catalog(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    def sort_key(e: Dict[str, Any]) -> Tuple[str, str]:
        return (e.get("name") or "", e.get("title") or "")

    return sorted(entries, key=sort_key)


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def write_csv(path: Path, entries: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "name",
        "title",
        "category",
        "origin",
        "originName",
        "apiVersion",
        "isDynamic",
        "blockJson",
        "hasRenderPhp",
        "hasIndexPhp",
        "hasViewJs",
        "sourceRoot",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for e in entries:
            writer.writerow(
                {
                    "name": e.get("name"),
                    "title": e.get("title"),
                    "category": e.get("category"),
                    "origin": e.get("origin"),
                    "originName": e.get("originName"),
                    "apiVersion": e.get("apiVersion"),
                    "isDynamic": e.get("derived", {}).get("isDynamic"),
                    "blockJson": e.get("filePaths", {}).get("blockJson"),
                    "hasRenderPhp": e.get("filePaths", {}).get("hasRenderPhp"),
                    "hasIndexPhp": e.get("filePaths", {}).get("hasIndexPhp"),
                    "hasViewJs": e.get("filePaths", {}).get("hasViewJs"),
                    "sourceRoot": e.get("sourceRoot"),
                }
            )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract WordPress block metadata.")
    parser.add_argument("--wp-root", required=True, help="Path to WordPress root directory")
    parser.add_argument("--wp-version", required=True, help="WordPress version label (e.g. 6.9.1)")
    parser.add_argument("--out-json", required=True, help="Output JSON path")
    parser.add_argument("--out-csv", help="Optional CSV output path")

    parser.add_argument(
        "--include-core",
        action="store_true",
        default=False,
        help="Include core blocks from wp-includes/blocks",
    )
    parser.add_argument(
        "--include-plugins",
        action="store_true",
        default=False,
        help="Include plugin blocks from wp-content/plugins",
    )
    parser.add_argument(
        "--include-mu-plugins",
        action="store_true",
        default=False,
        help="Include mu-plugin blocks from wp-content/mu-plugins",
    )
    parser.add_argument(
        "--include-themes",
        action="store_true",
        default=False,
        help="Include theme blocks from wp-content/themes",
    )
    parser.add_argument(
        "--extra-root",
        action="append",
        default=[],
        help="Additional root path to scan for block.json (repeatable)",
    )
    parser.add_argument(
        "--source-label",
        action="append",
        default=[],
        help="Optional labels for extra roots (repeatable; aligns with --extra-root)",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    wp_root = Path(args.wp_root).expanduser().resolve()
    if not wp_root.exists():
        raise SystemExit(f"wp-root does not exist: {wp_root}")

    roots: List[SourceRoot] = []

    if args.include_core:
        roots.append(SourceRoot("core", wp_root / "wp-includes" / "blocks"))
    if args.include_plugins:
        roots.append(SourceRoot("plugins", wp_root / "wp-content" / "plugins"))
    if args.include_mu_plugins:
        roots.append(SourceRoot("mu-plugins", wp_root / "wp-content" / "mu-plugins"))
    if args.include_themes:
        roots.append(SourceRoot("themes", wp_root / "wp-content" / "themes"))

    extra_labels = list(args.source_label)
    while len(extra_labels) < len(args.extra_root):
        extra_labels.append("extra")

    for label, path_str in zip(extra_labels, args.extra_root):
        roots.append(SourceRoot(label, Path(path_str).expanduser().resolve()))

    if not roots:
        raise SystemExit("No roots selected. Use --include-core or other include flags.")

    entries: List[Dict[str, Any]] = []
    for source_root, block_json in find_block_jsons(roots):
        data = safe_read_json(block_json)
        if not data:
            continue
        entries.append(build_entry(data, block_json, wp_root, source_root))

    entries = normalize_catalog(entries)

    payload = {
        "wordpressVersion": args.wp_version,
        "generatedAtUtc": utc_now_iso(),
        "wpRoot": str(wp_root),
        "sourceRoots": [
            {"label": r.label, "path": str(r.path)}
            for r in roots
        ],
        "blocks": entries,
    }

    out_json = Path(args.out_json).expanduser().resolve()
    write_json(out_json, payload)

    if args.out_csv:
        out_csv = Path(args.out_csv).expanduser().resolve()
        write_csv(out_csv, entries)


if __name__ == "__main__":
    main()
