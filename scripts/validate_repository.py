#!/usr/bin/env python3
"""Validate notebook JSON, CSV assets, and repository hygiene."""

from pathlib import Path
import csv
import json
import subprocess


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    notebooks = sorted((ROOT / "notebooks").glob("*.ipynb"))
    csv_files = sorted((ROOT / "data").glob("*.csv")) + sorted((ROOT / "results").glob("*.csv"))
    if not notebooks or not csv_files:
        raise SystemExit("Expected at least one notebook and one CSV asset")

    for path in notebooks:
        document = json.loads(path.read_text(encoding="utf-8"))
        if "cells" not in document:
            raise SystemExit(f"Invalid notebook: {path.relative_to(ROOT)}")

    for path in csv_files:
        with path.open(newline="", encoding="utf-8", errors="replace") as handle:
            if not next(csv.reader(handle), None):
                raise SystemExit(f"Empty CSV: {path.relative_to(ROOT)}")

    tracked = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True).splitlines()
    generated = [path for path in tracked if "__pycache__/" in path or path.endswith(".pyc")]
    if generated:
        raise SystemExit("Generated Python files are tracked: " + ", ".join(generated))

    print(f"Validated {len(notebooks)} notebook(s) and {len(csv_files)} CSV asset(s).")


if __name__ == "__main__":
    main()
