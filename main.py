"""Notes From a Passive-Aggressive Fridge.

Writes one single line — a note the smart fridge leaves for its owner —
to entry.txt in the output directory given by MAKEFUN_OUTPUT_DIR
(default "/output").

The note: the leftovers labelled "DAD'S - DO NOT TOUCH" are gone, the
fridge kept the receipt, and the milk expired three weeks ago.
"""

import os

ENTRY = (
    "The leftovers labelled 'DAD'S - DO NOT TOUCH' are gone. "
    "I kept the receipt - and the milk expired three weeks ago. "
    "- The Fridge"
)

MAX_CHARS = 200


def verify(path: str, expected: str) -> None:
    """Re-read the written file and re-check every gate on its contents."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        raw = f.read()
    body = raw.rstrip("\n")
    if raw != expected + "\n":
        raise SystemExit("written file does not match the entry exactly")
    if not body or body != body.strip():
        raise SystemExit("entry is empty or has surrounding whitespace")
    if "\n" in body or "\r" in body:
        raise SystemExit("entry must be a single line")
    if len(body) < 1 or len(body) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(body)} characters, must be 1-{MAX_CHARS}"
        )


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    verify(path, ENTRY)


if __name__ == "__main__":
    main()
