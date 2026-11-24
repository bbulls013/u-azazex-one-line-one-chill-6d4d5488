# One Line, One Chill

[![Competition](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/c/u-azazex-one-line-one-chill-6d4d5488)
[![Rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/bbulls013/u-azazex-one-line-one-chill-6d4d5488/rank.svg)](https://make.fun/c/u-azazex-one-line-one-chill-6d4d5488)
[![Reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/bbulls013/u-azazex-one-line-one-chill-6d4d5488/reward.svg)](https://make.fun/c/u-azazex-one-line-one-chill-6d4d5488)

A make.fun entry for [One Line, One Chill](https://make.fun/c/u-azazex-one-line-one-chill-6d4d5488):
one line of horror, a single sentence under 200 characters that frightens
in one breath.

## How it works

`main.py` is a small deterministic Python 3 program (standard library only).
It writes one fixed horror line to `/output/entry.txt` — no randomness, no
network, no clock, so every run produces the exact same bytes.

## The line

> A voicemail from my own number arrived at 3 a.m., and the voice on it —
> mine, older, out of breath — whispered, "Don't open the door; I already did."

The scare is earned, not announced: a concrete detail (a voicemail from your
own number, at 3 a.m.), a voice that is yours but older and out of breath,
and a last word that turns the whole sentence around. What it withholds —
whose door, what waits behind it, how the caller got your number — is what
keeps frightening after the line ends.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
