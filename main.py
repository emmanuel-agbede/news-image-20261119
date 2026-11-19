#!/usr/bin/env python3
"""make.fun entry for "news-image-20261119".

Copies the bundled news image (news.jpg, beside this file) byte-for-byte
to <output>/entry.png. The output directory is $MAKEFUN_OUTPUT_DIR when
set, otherwise /output. Standard library only.
"""

import os
import shutil
from pathlib import Path

ASSET = Path(__file__).resolve().parent / "news.jpg"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ASSET, out_dir / "entry.png")


if __name__ == "__main__":
    main()
