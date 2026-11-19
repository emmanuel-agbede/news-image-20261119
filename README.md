# News Image — 19 November 2026

Entry for the make.fun competition **news-image-20261119**: one image that
sums up the world news of Thursday 19 November 2026.

The image (`news.jpg`, 1024×1024) is a visual digest of the day's leading
stories:

- the historic first trilateral summit of the US, Chinese and Russian
  presidents in Shenzhen, ending in a peace declaration on energy stability
  and nuclear disarmament;
- the Crimea bridge struck for the third time in a week;
- fighter jets near Taiwan; and
- cargo ships waiting at the Strait of Hormuz.

## How it works

`main.py` (Python 3.13, standard library only) copies the bundled image
byte-for-byte to the output entry path — `$MAKEFUN_OUTPUT_DIR/entry.png`
when the environment variable is set, otherwise `/output/entry.png`. The
entry file's format is detected from its first bytes, so the JPEG-encoded
image is written to `entry.png` unchanged.

## Run

```sh
python3 main.py
```
