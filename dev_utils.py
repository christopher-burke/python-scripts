#!/usr/bin/env python3

"""Collection of Utilities."""

import requests
from shlex import quote, split
from subprocess import Popen, PIPE
from datetime import datetime
import logging
logging.basicConfig(level=logging.ERROR)


def say(phrase, time=True):
    """Say the time and phrase, using the macOS 'say' command."""
    command = None
    if time:
        now = datetime.now().strftime("%I:%M %p")
        now = f"It's {now}! "
    else:
        now = ""
        command = f"say {quote(now)}{quote(phrase)}"
        Popen(command, shell=True, stdout=PIPE)
    logging.debug(command)


def shell(*args):
    """Execute shell commands and return stdout."""
    logging.debug(args)
    command = args
    logging.debug(command)
    process = Popen(command, shell=True, stdout=PIPE)
    stdout, out = process.communicate()
    return stdout


def python_gitignore():
    """Pull latest Python.gitignore file from github."""
    URL = 'https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore'
    r = requests.get(URL)
    with open('Python.gitignore', 'wb') as f:
        f.write(r.content)
