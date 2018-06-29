#!/usr/bin/env python3

"""Collection of Utilities."""

import requests
from subprocess import Popen, PIPE
from datetime import datetime
import logging
logging.basicConfig(level=logging.DEBUG)


def say(phrase, time=True):
    """Say the time and phrase, using the macOS 'say' command."""
    if time:
        now = datetime.now().strftime("%I:%M %p")
        now = f"It's {now}! "
    else:
        now = ""
        Popen(f"say \"{now}{phrase}\".", shell=True, stdout=PIPE)
    logging.debug(f"say \"It's {now}! {phrase}\".")


def shell(*args):
    """Execute shell commands and return stdout."""
    process = Popen(args, stdout=PIPE)
    stdout, out = process.communicate()
    return stdout


def python_gitignore():
    """Pull latest Python.gitignore file from github."""
    URL = 'https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore'
    r = requests.get(URL)
    with open('Python.gitignore', 'wb') as f:
        f.write(r.content)
