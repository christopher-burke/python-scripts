#!/usr/bin/env python3

"""Take a Screenshot."""

import os
import pyscreeze
from datetime import datetime


def screenshot():
    """Take a screenshot."""
    filename = f'{datetime.now()}'
    pyscreeze.screenshot(filename + ".png")


if __name__ == '__main__':
    screenshot()
