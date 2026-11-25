"""Emoji writer: one fixed retry-loop emoji standing in for an AI agent."""

import os, sys

TEXT = "\U0001f501"
LIMIT = 16

def fail(msg):
    sys.stderr.write("invalid: " + msg + "\n")
    raise SystemExit(1)

def validate(text):
    rules = [
        (not text.strip(), "blank entry"),
        (len(text) > LIMIT, "over 16 characters"),
        (len(text) > 2, "more than one emoji"),
        (any(ord(c) < 32 or ord(c) == 127 for c in text), "control character found"),
        (text != text.strip() or " " in text or "\n" in text, "ragged edges, space, or newline"),
        (any(c.isascii() for c in text), "not an emoji"),
        (any(c.isalnum() for c in text), "has letters or digits"),
        (text == "\U0001f916", "the obvious robot"),
        (any(0xFE00 <= ord(c) <= 0xFE0F for c in text), "carries a variation selector"),
        ("\u200d" in text, "contains a zero-width joiner"),
    ]
    for bad, msg in rules:
        if bad:
            fail(msg)

def write_out():
    validate(TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TEXT + "\n")

if __name__ == "__main__":
    write_out()
