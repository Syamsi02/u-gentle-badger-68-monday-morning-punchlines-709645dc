"""Monday Morning Punchlines — one original joke about Monday mornings.

The program writes a single joke, no longer than 200 characters, to
/output/entry.txt. The joke is chosen for a twist the judge brief rewards:
not a plain complaint about Mondays, but a surprise turn — the alarm clock
itself filing a complaint — kept short so every word does work.
"""

import os
import sys

MAX_CHARS = 200

JOKE = (
    "My alarm filed for a restraining order this Monday — apparently being "
    "hit nine times before 7 a.m. counts as a hostile work environment, "
    "and even my coffee joined the complaint."
)


def validate(text):
    """Gate check, mirroring the bounty gate: 1-200 chars, not blank."""
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    return True


def main():
    if not validate(JOKE):
        print("joke fails the 1-200 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(JOKE)
    print("wrote %d characters to %s" % (len(JOKE), out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
