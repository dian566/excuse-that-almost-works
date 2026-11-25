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


def main() -> None:
    """Write the one-line excuse to /output/entry.txt."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
