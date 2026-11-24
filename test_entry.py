"""Tests for the Say What Actually Broke entry program (TDD: written
before main.py).

Behavior under test: running `python3 main.py` with $MAKEFUN_OUTPUT_DIR
pointing at an empty directory writes exactly one UTF-8 text file
entry.txt holding a single sentence of 1-200 characters, and two runs
produce byte-identical output (deterministic, no network, no randomness).
"""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent


def run_main(out_dir: Path) -> subprocess.CompletedProcess:
    env = dict(os.environ)
    env["MAKEFUN_OUTPUT_DIR"] = str(out_dir)
    return subprocess.run(
        [sys.executable, "main.py"],
        cwd=REPO,
        env=env,
        capture_output=True,
        text=True,
        timeout=30,
    )


def read_entry(out_dir: Path) -> str:
    entry = out_dir / "entry.txt"
    assert entry.is_file(), "entry.txt was not written"
    return entry.read_text(encoding="utf-8")


def test_entry_file_is_written():
    with tempfile.TemporaryDirectory() as tmp:
        result = run_main(Path(tmp))
        assert result.returncode == 0, f"main.py failed: {result.stderr}"
        assert (Path(tmp) / "entry.txt").is_file()


def test_entry_length_1_to_200_chars():
    with tempfile.TemporaryDirectory() as tmp:
        run_main(Path(tmp))
        text = read_entry(Path(tmp))
        assert 1 <= len(text) <= 200, f"length {len(text)} outside 1-200"
        assert text.strip(), "entry is only whitespace"


def test_entry_is_a_single_sentence():
    with tempfile.TemporaryDirectory() as tmp:
        run_main(Path(tmp))
        text = read_entry(Path(tmp)).strip()
        # Exactly one sentence: one terminal period, no other sentence ends.
        assert text.endswith("."), "entry must end with a period"
        assert text.count(".") == 1, "entry must be a single sentence"
        assert "?" not in text and "!" not in text


def test_entry_is_deterministic_across_runs():
    with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2:
        run_main(Path(d1))
        run_main(Path(d2))
        a = (Path(d1) / "entry.txt").read_bytes()
        b = (Path(d2) / "entry.txt").read_bytes()
        assert a == b, "two runs produced different bytes"
