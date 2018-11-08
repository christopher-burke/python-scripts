#!/usr/bin/env python3

"""Convert an image using Pillow.

requirements: Pillow

`pip install Pillow`.
"""

import os
from PIL import Image


def save_image(picture, dirpath, name, ext):
    """Save an image.

    :param picture: PIL.Image object
    :param dirpath: Directory to save image.
    :param name: Name of the image.
    :param ext: File extenstion to use.

    :return: None
    """
    name = name.rpartition('.')[0]
    picture.save(f'{dirpath}/{name}.{ext}')


def main(file):
    """Save an image in png format.

    This is an example function.

    :file: Full path of image file.
    :return: None
    """
    dirpath, _, filename = file.rpartition('/')
    picture = Image.open(file)
    save_image(picture, dirpath, filename, 'png')


if __name__ == "__main__":
    # Sample image source(https://unsplash.com/photos/70Rir5vB96U)
    file = os.path.realpath(
        'images/example/photo-1533709752211-118fcaf03312.jpeg')

    main(file)
