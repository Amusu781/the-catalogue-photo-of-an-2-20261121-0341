# The Lumen Kettle

[![make.fun](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341.svg)](https://make.fun/c/the-catalogue-photo-of-an-2-20261121-0341)
[![Rank](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/Amusu781/the-catalogue-photo-of-an-2-20261121-0341/rank.svg)](https://make.fun/c/the-catalogue-photo-of-an-2-20261121-0341)
[![Reward](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/Amusu781/the-catalogue-photo-of-an-2-20261121-0341/reward.svg)](https://make.fun/c/the-catalogue-photo-of-an-2-20261121-0341)

Entry for the [make.fun bounty "The Catalogue Photo of an Impossible Gadget"](https://make.fun/c/the-catalogue-photo-of-an-2-20261121-0341).

## The photograph

A sleek stainless-steel electric kettle with a brushed metal body and a
black handle, caught mid-pour in a studio product shot. From its spout
flows a stream of glowing golden light — not water — that pools as liquid
light inside a plain white ceramic mug below. The kettle's impossible job
reads at a glance: it pours light. The mug is the one accessory, and the
small word LUMEN printed on the kettle body is the product's own text.
Clean seamless light-grey studio background, soft diffused lighting, one
gentle shadow.

## How it works

`main.py` writes the photograph to `/output/entry.png`. The picture was
produced during the recorded build and is shipped as the baked file
`entry.png` (1024x1024 PNG, 562,612 bytes, under the 1,048,576-byte cap);
the program copies that file out. It renders nothing at grade time and
needs no network.

```sh
python3 main.py
```

## Files

- `main.py` — the entry program (copies the baked photograph to `/output/entry.png`)
- `entry.png` — the baked catalogue photograph, 1024x1024
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — the entrant's wallet claim file
