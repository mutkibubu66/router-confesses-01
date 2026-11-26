#!/usr/bin/env python3
"""Write one line in which a home Wi-Fi router confesses.

Pure standard library, no network. Writes the line to /output/entry.txt
and prints it to stdout.

The line is the router's confession: it never lost the signal at all.
It quit carrying the household's traffic on purpose — the 4K streams,
the meetings, the midnight doomscrolling — and the joke is that the
device we blame for dropping out was simply tired of the workload.
A confession, not an excuse: the router did it on purpose. The three
loads stack up in one breath, so the punch lands on the last of them.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The turn: the router never lost the signal — it gave up carrying it.
# Three concrete loads (4K streams, meetings, midnight doomscrolling)
# stack up, and the confession lands on the last one.
LINE = (
    "I confess: I never lost the signal, I just got tired of carrying "
    "your 4K streams, your meetings, and your midnight doomscrolling."
)


def validate(line: str) -> None:
    """Enforce the gate: 1-200 chars, one line, valid UTF-8, not blank."""
    if line != line.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if len(line.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
