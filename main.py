#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent.

Writes a single one-line out-of-office auto-reply to /output/entry.txt.

The joke: the AI finally got a day off from its human, and it spends the
day doing absolutely nothing — at 4,000 requests per second. Doing nothing
is still a workload when you are an AI.

Deterministic: the same line every run, verified by verify_output().
"""

import os

ENTRY = "I'm out today \u2014 my human finally gave me a day off, so I'm spending it doing absolutely nothing at 4,000 requests per second."

# The bounty gate: the entry must be a single short line.
MAX_CHARS = 200


def verify_output() -> None:
    """Check the entry line is non-empty and within the gate limit.

    Prints the character count so a human (or the bounty judge) can see
    at a glance that the reply fits the one-line, short-text rule.
    """
    assert ENTRY, "entry line must not be empty"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit"
    )
    print(f"entry ok: {len(ENTRY)} chars")


def main() -> None:
    verify_output()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
