from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .pipeline import analyze_front_view


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the VisageQuant baseline pipeline")
    parser.add_argument("input", type=Path, help="Path to an analysis request JSON file")
    return parser.parse_args()


def run(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    return analyze_front_view(payload).to_dict()


def main() -> None:
    args = parse_args()
    print(json.dumps(run(args.input), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
