"""Resignation note from the parking lot: one line, no encore."""

import os


def compose_note():
    pieces = [
        "I hereby resign as parking attendant:",
        "my own car was towed twice this month,",
        "and the second time it waved at me.",
    ]
    return " ".join(pieces)


def deliver(note):
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(note)


def run():
    note = compose_note()
    if not 1 <= len(note) <= 140:
        raise SystemExit("letter must be 1-140 characters, got %d" % len(note))
    deliver(note)


if __name__ == "__main__":
    run()
