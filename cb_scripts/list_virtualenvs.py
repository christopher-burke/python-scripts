#!/usr/bin/env python3

"""List all virtualenvs."""

import os
import socket


COMPUTER_NAME = socket.gethostname()
VIRTUAL_ENV = os.path.join(os.environ['HOME'], '.virtualenvs/')


for x in os.listdir(VIRTUAL_ENV):
    if os.path.isdir(os.path.join(VIRTUAL_ENV, x)):
        print(x)
