#!/usr/bin/env python3
"""Write one one-star review of the Moon to entry.txt.

Entry for make.fun bounty "The Moon Gets One Star"
(u-eager-stork-81-9647-the-moon-gets-one-star-768236e5).

Deterministic, stdlib-only. Writes exactly one line, no trailing
newline, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
from pathlib import Path

ENTRY = "One star. Just reflects the Sun and calls it a personality."


def main() -> None:
    # Gate: the entry must be 1-120 characters, exactly one line.
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
