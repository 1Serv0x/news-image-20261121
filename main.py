#!/usr/bin/env python3
"""Deliver the 21 November 2026 front page.

The entry is a picture, drawn beforehand and stored next to this file.
Running the program writes that picture to the grader's output folder
as entry.png. It needs no network and no packages beyond the standard
library, and because it writes the same stored bytes every time, the
grader's two runs produce identical files.
"""

import hashlib
import os
import sys
from pathlib import Path

IMAGE = "entry.png"


def main() -> int:
    root = Path(__file__).resolve().parent
    picture = root / IMAGE
    if not picture.exists():
        print(f"missing bundled image: {picture}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    data = picture.read_bytes()
    want = hashlib.sha256(data).hexdigest()
    target = out_dir / IMAGE
    target.write_bytes(data)
    if hashlib.sha256(target.read_bytes()).hexdigest() != want:
        print("written image does not match the bundled one", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
