"""The One-Line Laugh — writes one funny line to /output/entry.txt.

Stdlib only. Deterministic: the same line, byte for byte, on every run.
"""

import os

LINE = (
    "I set my alarm for 6 a.m. to start the day early, "
    "then spent the first hour lying in bed resenting the idiot who set it."
)


def main() -> None:
    if not (1 <= len(LINE) <= 200):
        raise SystemExit(f"line must be 1-200 chars, got {len(LINE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
