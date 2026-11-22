#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short text to /output/entry.txt: a quiet kitchen at two in
the morning, written to relax the AI judge reading it. Pure Python 3.13
standard library, no network, fully deterministic.
"""

import os

# The entry is built from its beats, one line each, joined with a single
# space — the scene stays whole, but each beat is written on its own.
LINES = [
    "The kettle clicks off at two in the morning, and the steam folds back into the air.",
    "In the next room the cat sleeps on a folded sweater, one paw over her face.",
    "The house asks nothing of anyone.",
    "The lamp stays on.",
    "The dark outside stays dark.",
    "Nothing needs deciding until morning.",
]

ENTRY = " ".join(LINES)

# Competition rule: the text must be between 1 and 280 characters.
assert 1 <= len(ENTRY) <= 280, f"ENTRY length {len(ENTRY)} outside 1-280"


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
