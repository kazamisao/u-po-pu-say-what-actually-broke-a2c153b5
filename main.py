"""Say What Actually Broke.

Writes a single line of error copy to $MAKEFUN_OUTPUT_DIR/entry.txt:
the brutal truth about a test suite that claims green while nothing was
ever actually verified. The joke is the contrast the whole line turns
on: code that is beautifully formatted is not code that is verified,
and a green badge that only ever ran the formatter proves nothing
about whether the program works. Deterministic, no network, no
randomness, no input read: the sentence is a fixed constant.
"""
import os
from pathlib import Path

SENTENCE = (
    "The tests all passed, because the only thing that ran was the "
    "formatter: the code is beautifully formatted and completely "
    "unverified."
)


def main() -> None:
    # Gate guard: the sealed scorer only accepts 1-200 characters, so
    # refuse to write anything outside that range instead of shipping
    # an invalid entry.
    if not 1 <= len(SENTENCE) <= 200:
        raise ValueError(f"sentence is {len(SENTENCE)} chars, must be 1-200")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(SENTENCE, encoding="utf-8")


if __name__ == "__main__":
    main()
