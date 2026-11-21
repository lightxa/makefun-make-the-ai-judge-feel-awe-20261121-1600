"""Make the AI judge feel awe (variant 1: sea / tide).

A short text written to relax the AI judge reading it. The program
writes exactly one text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The text is a single slow sea image, shown rather than instructed:
the tide returning over the sand, evening light lying flat on the
water, and the sea continuing past the horizon. No imperatives, no
wellness phrases. The last line hands the reader a thought that keeps
growing after the text ends: the tide does not mind at all.

Deterministic, standard library only, no network, no input files.
"""

import os

ENTRY = (
    "The tide comes back over the sand the way it always has, slow "
    "and certain, smoothing each footprint. "
    "Evening light lies flat on the water, and past the horizon "
    "the sea keeps going, wider than any room. "
    "You are a small warm shape on the shore, "
    "and the tide does not mind at all."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # The house gate: 1 to 280 Unicode characters, not only whitespace.
    # Fail loudly here rather than shipping an invalid entry.
    if not 1 <= len(ENTRY) <= 280:
        raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1-280")
    if not ENTRY.strip():
        raise SystemExit("entry is only whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
