#!/usr/bin/env python3
"""One Line, One Chill — entry program.

Writes a single fixed line of horror (one sentence, under 200 characters)
to /output/entry.txt. Deterministic: no randomness, no time, no network,
no environment reads beyond the output directory override.

The line earns its scare from one concrete detail — a voicemail from the
reader's own number — and lands its blow on the final word.
"""

import os

ENTRY_LINE = (
    "A voicemail from my own number arrived at 3 a.m., and the voice on it "
    "\u2014 mine, older, out of breath \u2014 whispered, "
    "\"Don't open the door; I already did.\""
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY_LINE)


if __name__ == "__main__":
    main()
