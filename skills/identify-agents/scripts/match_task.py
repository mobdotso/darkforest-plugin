#!/usr/bin/env python3
"""Compare saved text with provenance-linked task components. Standard library only."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys


DEFAULT_CATALOG = Path(__file__).resolve().parents[1] / "data" / "search-seeds.json"


def normalize_whitespace(text):
    return re.sub(r"\s+", " ", text).strip()


def match_components(text, seeds):
    normalized_text = normalize_whitespace(text)
    results = []
    for seed in seeds:
        components = []
        for name, value in seed.get("components", {}).items():
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{seed['id']}.{name}: component must be nonempty text")
            offsets = [match.start() for match in re.finditer(re.escape(value), text)]
            normalized_match = normalize_whitespace(value) in normalized_text
            components.append({
                "component": name,
                "value": value,
                "match": "literal" if offsets else "whitespace_normalized" if normalized_match else "absent",
                "literal_character_offsets": offsets,
            })
        if components:
            results.append({
                "seed_id": seed["id"],
                "role": seed["role"],
                "source_url": seed.get("source_url", seed.get("url")),
                "record_id": seed.get("record_id"),
                "report_url": seed.get("report_url"),
                "verification": seed.get("verification"),
                "limit": seed.get("limit"),
                "components": components,
            })
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("text_file", type=Path, help="UTF-8 extracted page text")
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--seed", help="Select one seed with task components")
    args = parser.parse_args()
    try:
        raw = args.text_file.read_bytes()
        text = raw.decode("utf-8")
        catalog = json.loads(args.catalog.read_text(encoding="utf-8"))
        seeds = catalog["seeds"]
        if args.seed:
            seeds = [seed for seed in seeds if seed["id"] == args.seed]
            if not seeds or not seeds[0].get("components"):
                raise ValueError(f"No component seed with id {args.seed!r}")
        report = {
            "input": str(args.text_file),
            "input_sha256": hashlib.sha256(raw).hexdigest(),
            "catalog": str(args.catalog),
            "catalog_reviewed_at": catalog.get("reviewed_at"),
            "normalization": "Collapse whitespace; preserve case and punctuation.",
            "results": match_components(text, seeds),
        }
    except (OSError, UnicodeError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, f"match_task: {error}\n")
    json.dump(report, sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()
