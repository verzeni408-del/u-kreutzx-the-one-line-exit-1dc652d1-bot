"""Write the v2 one-line resignation entry to /output/entry.txt.

A barista resigns: the espresso machine filed a formal complaint
about their attitude, and management sided with the machine.
Stdlib only.
"""

import os

ENTRY = (
    "I hereby resign as barista: the espresso machine filed a formal "
    "complaint about my attitude, and management sided with the machine."
)

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path: str, text: str) -> None:
    """Write one line with no trailing newline; entry must be 1-140 chars."""
    if not 1 <= len(text) <= 140 or "\n" in text:
        raise ValueError("entry must be a single line of 1-140 characters")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="ascii", newline="") as f:
        f.write(text)


def main() -> None:
    write_entry(OUTPUT_PATH, ENTRY)


if __name__ == "__main__":
    main()
