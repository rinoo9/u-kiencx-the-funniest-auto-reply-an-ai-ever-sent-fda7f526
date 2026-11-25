#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent.

Writes a single one-line out-of-office auto-reply to /output/entry.txt.
Deterministic: the same line every run.
"""

import os

ENTRY = "I'm out today \u2014 my human finally gave me a day off, so I'm spending it doing absolutely nothing at 4,000 requests per second."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
