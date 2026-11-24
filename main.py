"""One-line resignation letter generator.

Writes a single-line resignation letter to /output/entry.txt.
Stdlib only. No trailing newline, one line, 1-140 characters.
"""

import os

LETTER = (
    "I hereby resign as night security guard: the ghost in aisle 3 clocks "
    "in on time, never sleeps, and asked for my parking spot."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
