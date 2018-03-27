#!/usr/bin/env python3

"""Move files to another folder."""

import sys
import os
import shutil
import logging


logging.basicConfig(level=logging.DEBUG)


def move(srcdir, dstdir):
    """Move files from Source Directory to Destination Directory."""
    files = os.listdir(srcdir)

    for file_ in files:
        shutil.move(os.path.join(srcdir, file_), dstdir)
        logging.debug(f"{file_} moved to {dstdir}.")


if __name__ == "__main__":
    srcdir = sys.argv[1]
    dstdir = sys.argv[2]
    move(srcdir, dstdir)
