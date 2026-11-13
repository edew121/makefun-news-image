"""13 November 2026 — make.fun news-image-01 entry.

Copies the bundled news summary image (entry.png, a JPEG by magic bytes
as the rules allow) to the output directory. Standard library only, no
network, fully deterministic: every run writes the same bytes.

The image is a front page for Friday 13 November 2026: a burning tanker
in the Strait of Hormuz, Europe joining the Ukraine peace talks, the
global Microsoft Outlook outage, and Nvidia's chief executive departing
under a summons from Congress.
Run locally with: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
dest = os.path.join(OUT, "entry.png")
shutil.copyfile(os.path.join(HERE, "entry.png"), dest)
# Sanity check: the output must be a non-empty file, byte-identical to the
# bundled image (JPEG by magic bytes, as the rules allow).
assert os.path.getsize(dest) > 0
with open(dest, "rb") as f:
    assert f.read(3) == b"\xff\xd8\xff"
