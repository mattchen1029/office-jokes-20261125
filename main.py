#!/usr/bin/env python3
"""Entry for make.fun's 'Make the AI Judge Laugh: Office Jokes'.

Writes one one-line office joke to /output/entry.txt.
The joke must be UTF-8 text of 1 to 199 characters.
"""

import os

JOKE = (
    "I finally got my inbox to zero, and then IT sent a company-wide email "
    "congratulating us on inbox zero, which put my inbox back to one."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
