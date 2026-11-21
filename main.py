#!/usr/bin/env python3
"""The Lumen Kettle — entry program.

Copies the baked catalogue photograph (entry.png, sitting next to
this file) into the output directory. Nothing is rendered or
generated at grade time: the image is shipped with the entry and
only copied here. No network access is used.
"""

import os
import shutil
import struct
import sys

MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024
SOURCE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"


def read_png_dimensions(path):
    """Return (width, height) parsed from the PNG IHDR chunk."""
    with open(path, "rb") as handle:
        header = handle.read(33)
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("baked image is not a PNG file")
    if header[12:16] != b"IHDR":
        raise ValueError("baked PNG has no IHDR chunk where expected")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def clear_directory_contents(directory):
    """Remove every entry inside directory, leaving the directory itself.

    The grader mounts the output directory read-only and runs this
    program as an unprivileged user, so deleting the directory itself
    would fail; only its contents are ever removed.
    """
    for name in os.listdir(directory):
        target = os.path.join(directory, name)
        if os.path.isdir(target) and not os.path.islink(target):
            shutil.rmtree(target)
        else:
            os.remove(target)


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)

    if not os.path.isfile(source):
        print(f"error: baked image not found: {source}", file=sys.stderr)
        return 1

    size = os.path.getsize(source)
    if size > MAX_BYTES:
        print(
            f"error: baked image is {size} bytes, over the "
            f"{MAX_BYTES} byte limit",
            file=sys.stderr,
        )
        return 1

    width, height = read_png_dimensions(source)
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        print(
            f"error: baked image is {width}x{height}, over the "
            f"{MAX_DIMENSION}x{MAX_DIMENSION} limit",
            file=sys.stderr,
        )
        return 1

    os.makedirs(output_dir, exist_ok=True)
    clear_directory_contents(output_dir)

    destination = os.path.join(output_dir, OUTPUT_NAME)
    shutil.copyfile(source, destination)

    print(f"output: {destination}")
    print(f"dimensions: {width}x{height}")
    print(f"bytes: {size}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
