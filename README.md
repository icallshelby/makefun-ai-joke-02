# AI Joke — Clipboard With a Salary

Entry for the make.fun bounty `ai-joke-02` ("Make the AI judge laugh").

`main.py` (Python 3, standard library only, no network) writes one fixed
joke — a one-liner about AI coding agents — to `entry.txt` in
`$MAKEFUN_OUTPUT_DIR` (else `/output`):

> I used to write the code. Now I copy error messages into my coding
> agent and copy its fixes back into the terminal. I'm not a developer
> anymore; I'm a clipboard with a salary.

The joke is a constant, so the program is deterministic: two runs write
byte-identical output, well inside the gate's limits (UTF-8, 1–280
characters, not only white space) and the 60-second runtime budget.

The angle: the daily reality of working beside a coding agent is
shuttling error messages and fixes back and forth between the terminal
and the agent — the human demoted to a peripheral device. See
`BUILD-REPORT.md` for the candidate jokes considered and the local
verification.
