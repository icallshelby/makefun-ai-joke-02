#!/usr/bin/env python3
"""Entry for make.fun bounty ai-joke-02 ("Make the AI judge laugh").

This program is only a delivery mechanism for one fixed one-liner
about working beside an AI coding agent: every run writes exactly
the same bytes to entry.txt inside $MAKEFUN_OUTPUT_DIR (which stands
in for /output outside the grader). Standard library only; no
network, no clock, no randomness -- nothing varies between runs,
so the grader's two runs see identical output.

The judging gate counts the file in Unicode code points and allows
1 to 280 of them, at least one of them not white space. The joke is
written with no trailing newline, so the file holds the joke and
nothing else.
"""
import os

JOKE = (
    "I used to fear my coding agent would take my job. Now I fear "
    "standup, where I have to present its work in the first person."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
