# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/competitions/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/kazamisao/u-po-pu-say-what-actually-broke-a2c153b5/rank.svg)](https://make.fun/competitions/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/kazamisao/u-po-pu-say-what-actually-broke-a2c153b5/reward.svg)](https://make.fun/competitions/u-po-pu-say-what-actually-broke-a2c153b5)

Entry for the [make.fun](https://make.fun) competition
**Say What Actually Broke**
(`u-po-pu-say-what-actually-broke-a2c153b5`).

## What it does

`main.py` writes a single line of error copy (133 characters) to
`$MAKEFUN_OUTPUT_DIR/entry.txt` — the brutal truth about a test suite
that claims green while nothing was ever verified. It is fully
deterministic: no network, no randomness, no input read.

> The tests all passed, because the only thing that ran was the formatter: the code is beautifully formatted and completely unverified.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Tests

`test_entry.py` checks the entry file is written, holds 1–200
characters as a single sentence, and is byte-identical across two runs.
Run it with plain Python (no pytest needed):

```sh
python3 -c "import test_entry; [getattr(test_entry, n)() for n in sorted(dir(test_entry)) if n.startswith('test_')]"
```
