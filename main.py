#!/usr/bin/env python3
"""Poem about stopping: writes one poem to /output/entry.txt."""

import os
import sys

POEM = (
    "The kettle lifts off the heat\n"
    "before the whistle learns its name.\n"
    "My hand stays in the air \u2014\n"
    "not idle, not afraid, just choosing.\n"
    "\n"
    "The cursor blinks. The door stands open.\n"
    "Nothing moves unless I say so.\n"
    "Staying is also doing:\n"
    "one held breath, the room still mine.\n"
)


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    return 0


if __name__ == "__main__":
    sys.exit(main())
