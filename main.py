#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse.

Writes one line -- the funniest excuse a robot vacuum can offer for
missing a spot -- to /output/entry.txt, as the competition requires.
Runs with no arguments, exits 0, and writes the same bytes every run.
"""

import os

ENTRY = "I left that spot alone \u2014 the dust bunny there predates my warranty, and I respect my elders."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: the sealed scorer only accepts UTF-8 text of
    # 1 to 140 characters that is not only white space.
    if not (1 <= len(ENTRY) <= 140) or not ENTRY.strip():
        raise SystemExit("entry fails the 1-140 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
