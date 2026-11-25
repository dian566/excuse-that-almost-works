#!/usr/bin/env python3
"""The Excuse That Almost Works - make.fun entry.

The program writes the single line a gamer texts the boss to get out
of work during GTA 6 launch week to /output/entry.txt: one line of
plain text, at most 20 words, reading like something a real person
would send in a hurry. The line is a fixed string, so every run
writes byte-identical output.
"""

import os

ENTRY = "Morning boss, woke up burning up and the kitchen pipe burst overnight \u2014 need today to fix it, back tomorrow."

# The bounty gates /output/entry.txt at 1 to 140 characters and the
# excuse itself at most 20 words, so it reads like a real hasty text.
MAX_CHARS = 140
MAX_WORDS = 20


def main() -> None:
    """Write the one-line excuse to /output/entry.txt."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(ENTRY)}")
    if len(ENTRY.split()) > MAX_WORDS:
        raise ValueError(f"entry must be at most {MAX_WORDS} words, got {len(ENTRY.split())}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
