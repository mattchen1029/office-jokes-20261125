#!/usr/bin/env python3
"""Entry for make.fun's 'Make the AI Judge Laugh: Office Jokes'.

Writes one one-line office joke to /output/entry.txt.
The competition gate requires UTF-8 text of 1 to 199 characters; this
program checks that gate itself before writing, so an invalid entry
fails loudly here instead of being scored 0 by the sealed scorer.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 199

JOKE = (
    "I finally got my inbox to zero, and then IT sent a company-wide email "
    "congratulating us on inbox zero, which put my inbox back to one."
)


def validate_joke(joke: str) -> None:
    """Fail loudly if the joke would fail the competition's gate."""
    n = len(joke)
    if not (MIN_CHARS <= n <= MAX_CHARS):
        raise ValueError(
            f"joke is {n} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if not joke.strip():
        raise ValueError("joke must not be only whitespace")


def write_entry(joke: str) -> None:
    validate_joke(joke)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(joke)


def main() -> None:
    try:
        write_entry(JOKE)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
