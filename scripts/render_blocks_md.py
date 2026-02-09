#!/usr/bin/env python3
"""Render a Markdown catalog from a block metadata JSON file."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def stringify(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=True)


def render_attributes(attrs: Dict[str, Any]) -> str:
    if not attrs:
        return "_None_\n"

    lines = ["| Name | Type | Default | Source | Selector / Attr |", "|---|---|---:|---|---|"]
    for name in sorted(attrs.keys()):
        info = attrs.get(name, {}) or {}
        attr_type = stringify(info.get("type"))
        default = stringify(info.get("default"))
        source = stringify(info.get("source"))
        selector = stringify(info.get("selector"))
        attribute = stringify(info.get("attribute"))

        selector_attr = ""
        if selector and attribute:
            selector_attr = f"{selector} | {attribute}"
        elif selector:
            selector_attr = selector
        elif attribute:
            selector_attr = attribute

        lines.append(
            f"| {name} | {attr_type} | {default} | {source} | {selector_attr} |"
        )

    return "\n".join(lines) + "\n"


def render_supports(supports: Dict[str, Any]) -> str:
    if not supports:
        return "_None_\n"
    return "```json\n" + json.dumps(supports, indent=2, sort_keys=True) + "\n```\n"


def render_block(block: Dict[str, Any], examples: Dict[str, Any]) -> str:
    name = stringify(block.get("name"))
    title = stringify(block.get("title"))
    category = stringify(block.get("category"))
    api_version = stringify(block.get("apiVersion"))
    origin = stringify(block.get("origin"))
    origin_name = stringify(block.get("originName"))
    is_dynamic = stringify(block.get("derived", {}).get("isDynamic"))

    header = [f"## {name}"]
    header.append(f"**Title:** {title}")
    header.append(f"**Category:** {category}")
    header.append(f"**API Version:** {api_version}")

    if origin_name:
        header.append(f"**Origin:** {origin} ({origin_name})")
    else:
        header.append(f"**Origin:** {origin}")

    header.append(f"**Dynamic:** {is_dynamic}")

    parts = ["\n".join(header), ""]

    parts.append("### Attributes")
    parts.append(render_attributes(block.get("attributes", {})))

    parts.append("### Supports")
    parts.append(render_supports(block.get("supports", {})))

    parts.append("### Example Markup")
    example_entry = examples.get(name) if examples else None
    if example_entry and example_entry.get("markup"):
        parts.append("```html")
        parts.append(example_entry.get("markup"))
        parts.append("```\n")
        variants = example_entry.get("variants", [])
        if variants:
            parts.append("#### Variants")
            for variant in variants:
                label = stringify(variant.get("label")) or "Variant"
                markup = variant.get("markup") or ""
                parts.append(f"**{label}**")
                parts.append("```html")
                parts.append(markup)
                parts.append("```\n")
    else:
        parts.append("_Not generated yet._\n")

    return "\n".join(parts)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render Markdown from block catalog JSON.")
    parser.add_argument("--in-json", required=True, help="Input JSON path")
    parser.add_argument("--out-md", required=True, help="Output Markdown path")
    parser.add_argument("--examples-json", help="Optional examples JSON path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    in_path = Path(args.in_json).expanduser().resolve()
    out_path = Path(args.out_md).expanduser().resolve()

    payload = read_json(in_path)
    blocks: List[Dict[str, Any]] = payload.get("blocks", [])
    examples_payload: Dict[str, Any] = {}
    examples: Dict[str, Any] = {}
    if args.examples_json:
        examples_payload = read_json(Path(args.examples_json).expanduser().resolve())
        examples = examples_payload.get("examples", {})

    wp_version = stringify(payload.get("wordpressVersion"))
    plugin_slug = stringify(payload.get("pluginSlug"))
    plugin_version = stringify(payload.get("pluginVersion"))
    source_roots = payload.get("sourceRoots", [])
    source_str = ", ".join([f"{r.get('label')}: {r.get('path')}" for r in source_roots])

    lines: List[str] = []
    lines.append("---")
    lines.append(f"wordpress_version: {wp_version}")
    lines.append(f"generated_at_utc: {utc_now_iso()}")
    if plugin_slug:
        lines.append(f"plugin_slug: {plugin_slug}")
    if plugin_version:
        lines.append(f"plugin_version: {plugin_version}")
    if source_str:
        lines.append(f"source_roots: {source_str}")
    lines.append("---")
    lines.append("")
    if plugin_slug and plugin_version:
        lines.append(f"# WordPress Blocks Catalog (WP {wp_version}, {plugin_slug} {plugin_version})")
    elif plugin_slug:
        lines.append(f"# WordPress Blocks Catalog (WP {wp_version}, {plugin_slug})")
    else:
        lines.append(f"# WordPress Blocks Catalog ({wp_version})")
    lines.append("")

    for block in blocks:
        lines.append(render_block(block, examples))
        lines.append("---")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
