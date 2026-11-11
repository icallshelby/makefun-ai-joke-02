#!/usr/bin/env python3
"""Entry for make.fun bounty ai-joke-02 ("Make the AI judge laugh").

Writes one fixed joke -- a one-liner about AI coding agents -- to
entry.txt in the output directory ($MAKEFUN_OUTPUT_DIR, else /output).
Python standard library only, no network, no clock, no randomness:
every run writes exactly the same bytes.

The gate (RULES.txt): the file must be UTF-8, hold 1 to 280 characters
counted as Unicode code points, and not be only white space. The joke
below is written with no trailing line end, so the judge sees exactly
the joke and nothing else.
"""
import os

JOKE = (
    "I used to write the code. Now I copy error messages into my coding "
    "agent and copy its fixes back into the terminal. I'm not a developer "
    "anymore; I'm a clipboard with a salary."
)


def main():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, 'entry.txt'), 'w', encoding='utf-8') as fh:
        fh.write(JOKE)


if __name__ == '__main__':
    main()
