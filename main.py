"""The Perfect Pickup Line — make.fun entry.

Reads the single pickup line from entry.txt and hands it to the
judge harness by writing it to /output/entry.txt.
"""

import os


def load_line():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), encoding="utf-8") as fh:
        return fh.read().strip()


def main():
    line = load_line()
    # The sealed gate only accepts 1-200 non-blank UTF-8 characters.
    if not 1 <= len(line) <= 200 or not line.strip():
        raise SystemExit("entry.txt must hold one line of 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)
    print(line)


if __name__ == "__main__":
    main()
