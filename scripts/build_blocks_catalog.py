#!/usr/bin/env python3
"""Build block catalog artifacts and Markdown docs.

Optionally downloads a WordPress release tarball if a wp-root is not provided.
"""

from __future__ import annotations

import argparse
import tarfile
import urllib.request
from pathlib import Path


DEFAULT_TARBALL = "https://wordpress.org/wordpress-{version}.tar.gz"


def download_tarball(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as r, open(dest, "wb") as f:
        f.write(r.read())


def extract_tarball(tgz: Path, dest_dir: Path) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    with tarfile.open(tgz, "r:gz") as tar:
        tar.extractall(path=dest_dir)
    return dest_dir / "wordpress"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build WordPress block catalog artifacts.")
    parser.add_argument("--wp-version", required=True, help="WordPress version, e.g. 6.9.1")
    parser.add_argument("--wp-root", help="Path to local WordPress root directory")
    parser.add_argument("--download", action="store_true", help="Download WordPress release tarball")
    parser.add_argument("--download-url", help="Override tarball URL")

    parser.add_argument("--include-plugins", action="store_true", default=False)
    parser.add_argument("--include-mu-plugins", action="store_true", default=False)
    parser.add_argument("--include-themes", action="store_true", default=False)
    parser.add_argument("--extra-root", action="append", default=[])
    parser.add_argument("--source-label", action="append", default=[])
    parser.add_argument("--examples-json", help="Optional examples JSON to merge into Markdown output")
    parser.add_argument(
        "--split-by-origin",
        action="store_true",
        default=False,
        help="Generate separate docs/artifacts for core, plugins, and themes.",
    )
    parser.add_argument(
        "--plugin-filter",
        action="append",
        default=[],
        help="Optional plugin slug to split into its own {plugin}-blocks.md (repeatable).",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    artifacts_dir = repo_root / "artifacts"
    docs_dir = repo_root / "docs"

    wp_root: Path
    tmp_dir = None

    if args.wp_root:
        wp_root = Path(args.wp_root).expanduser().resolve()
    elif args.download:
        tmp_dir = artifacts_dir / f"wp-{args.wp_version}-src"
        tarball_url = args.download_url or DEFAULT_TARBALL.format(version=args.wp_version)
        tarball_path = artifacts_dir / f"wordpress-{args.wp_version}.tar.gz"

        download_tarball(tarball_url, tarball_path)
        wp_root = extract_tarball(tarball_path, tmp_dir)
    else:
        raise SystemExit("Provide --wp-root or use --download")

    import subprocess
    import json
    import csv

    def run_extract(out_json: Path, out_csv: Path, includes: list[str]) -> None:
        cmd = [
            "python3",
            str(repo_root / "scripts" / "extract_blocks_catalog.py"),
            "--wp-root",
            str(wp_root),
            "--wp-version",
            args.wp_version,
            "--out-json",
            str(out_json),
            "--out-csv",
            str(out_csv),
        ]
        cmd.extend(includes)
        for extra_root in args.extra_root:
            cmd.extend(["--extra-root", extra_root])
        for label in args.source_label:
            cmd.extend(["--source-label", label])
        subprocess.run(cmd, check=True)

    def run_render(in_json: Path, out_md: Path) -> None:
        cmd = [
            "python3",
            str(repo_root / "scripts" / "render_blocks_md.py"),
            "--in-json",
            str(in_json),
            "--out-md",
            str(out_md),
        ]
        if args.examples_json:
            cmd.extend(["--examples-json", args.examples_json])
        subprocess.run(cmd, check=True)

    def write_filtered(json_in: Path, json_out: Path, csv_out: Path, predicate) -> None:
        payload = json.loads(json_in.read_text(encoding="utf-8"))
        blocks = [b for b in payload.get("blocks", []) if predicate(b)]
        payload["blocks"] = blocks
        json_out.parent.mkdir(parents=True, exist_ok=True)
        json_out.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

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
        csv_out.parent.mkdir(parents=True, exist_ok=True)
        with csv_out.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            for e in blocks:
                w.writerow(
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


    if args.split_by_origin:
        # Core
        core_json = artifacts_dir / f"wp-{args.wp_version}-core-blocks.json"
        core_csv = artifacts_dir / f"wp-{args.wp_version}-core-blocks.csv"
        core_md = docs_dir / f"wp-{args.wp_version}-core-blocks.md"
        run_extract(core_json, core_csv, ["--include-core"])
        run_render(core_json, core_md)

        # Plugins
        if args.include_plugins or args.include_mu_plugins:
            plugin_json = artifacts_dir / f"wp-{args.wp_version}-plugin-blocks.json"
            plugin_csv = artifacts_dir / f"wp-{args.wp_version}-plugin-blocks.csv"
            plugin_md = docs_dir / f"wp-{args.wp_version}-plugin-blocks.md"
            includes = []
            if args.include_plugins:
                includes.append("--include-plugins")
            if args.include_mu_plugins:
                includes.append("--include-mu-plugins")
            run_extract(plugin_json, plugin_csv, includes)
            run_render(plugin_json, plugin_md)

            # Split specific plugins into their own docs/artifacts.
            for plugin_slug in args.plugin_filter:
                slug = plugin_slug.strip()
                if not slug:
                    continue
                out_json = artifacts_dir / f"wp-{args.wp_version}-{slug}-blocks.json"
                out_csv = artifacts_dir / f"wp-{args.wp_version}-{slug}-blocks.csv"
                out_md = docs_dir / f"{slug}-blocks.md"
                write_filtered(
                    plugin_json,
                    out_json,
                    out_csv,
                    lambda b, s=slug: b.get("origin") == "plugin"
                    and b.get("originName") == s,
                )
                run_render(out_json, out_md)

        # Themes
        if args.include_themes:
            theme_json = artifacts_dir / f"wp-{args.wp_version}-theme-blocks.json"
            theme_csv = artifacts_dir / f"wp-{args.wp_version}-theme-blocks.csv"
            theme_md = docs_dir / f"wp-{args.wp_version}-theme-blocks.md"
            run_extract(theme_json, theme_csv, ["--include-themes"])
            run_render(theme_json, theme_md)
    else:
        json_out = artifacts_dir / f"wp-{args.wp_version}-core-blocks.json"
        csv_out = artifacts_dir / f"wp-{args.wp_version}-core-blocks.csv"
        md_out = docs_dir / f"wp-{args.wp_version}-core-blocks.md"
        includes = ["--include-core"]
        if args.include_plugins:
            includes.append("--include-plugins")
        if args.include_mu_plugins:
            includes.append("--include-mu-plugins")
        if args.include_themes:
            includes.append("--include-themes")
        run_extract(json_out, csv_out, includes)
        run_render(json_out, md_out)


if __name__ == "__main__":
    main()
