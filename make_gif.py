#!/usr/bin/env python3

"""Create gif from directory."""

import imageio
import pathlib
import sys
import logging
logging.basicConfig(level=logging.CRITICAL)


def create_gif(file_iterator, duration=2, output='out.gif'):
    """Create gif from an iterator of files."""
    frames = []
    for file_ in file_iterator:
        if file_.suffix.lower() in ('.jpg', '.jpeg', '.png'):
            frames.append(imageio.imread(file_))
    logging.debug(frames)
    imageio.mimsave(output, frames, duration=duration)


if __name__ == "__main__":
    path = sys.argv[1]
    p = pathlib.Path(path)
    create_gif(p.iterdir())
