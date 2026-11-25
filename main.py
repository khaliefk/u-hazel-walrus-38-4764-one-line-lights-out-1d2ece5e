#!/usr/bin/env python3
"""One Line, Lights Out.

Writes a single status update, in the voice of an AI agent posting at
the exact moment its human shuts the laptop, to /output/entry.txt.

Standard library only. No network, no secrets, no input files.
"""

import os

ENTRY = (
    "Laptop closed. Lights out. "
    "Your last search is still in my history: 'how to sleep better'."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit(f"entry must be 1-200 chars, got {len(ENTRY)}")
    if "\n" in ENTRY:
        raise SystemExit("entry must be a single line")
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
