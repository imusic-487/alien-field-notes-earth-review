# Alien Field Notes: The Two Day Earth Review

[![make.fun bounty](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/imusic-487/alien-field-notes-earth-review/rank.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/imusic-487/alien-field-notes-earth-review/reward.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

Entry for the [make.fun bounty "Alien Field Notes: The Two Day Earth Review"](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000).

## The review

> The locals point glowing rectangles at their food before eating it, like asking the meal for permission. Polite species. 4/5, would orbit again.

144 characters, one line. An alien tourist watches humans photograph their
dinner before touching it and reads the ritual as good manners — the
meal is asked for permission first — then leaves a verdict and a rating,
like a real travel review.

## How it works

`main.py` (Python 3.13 standard library only, no network) writes the review
to `/output/entry.txt`:

```sh
python3 main.py
```

It self-checks the competition gate first: 1–200 characters, a single line,
not only whitespace. The output is deterministic — every run writes the
exact same bytes.
