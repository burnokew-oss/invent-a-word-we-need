#!/usr/bin/env python3
"""Invent a Word We Need -- entry program.

Writes one invented English word and its one-line definition to
/output/entry.txt: the whole entry is a single line of at most
140 characters. Pure standard library, deterministic: the same
word and definition on every run.
"""

import os

ENTRY = "appnesia \u2014 opening an app and forgetting why you opened it."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 140):
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
