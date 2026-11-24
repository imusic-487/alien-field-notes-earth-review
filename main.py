#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line — a review of planet Earth left by an alien
tourist — to /output/entry.txt. Python 3.13 standard library only,
no network, deterministic: every run writes the exact same bytes.
"""

import os

ENTRY = (
    "The locals point glowing rectangles at their food before eating it, "
    "like asking the meal for permission. Polite species. 4/5, would orbit again."
)


def main() -> None:
    text = ENTRY
    # Self-check the competition gate: 1-200 characters, a single line,
    # not only whitespace.
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text and text.strip(), "entry must be one non-blank line"
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {out}")


if __name__ == "__main__":
    main()
