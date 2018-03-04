#!/usr/bin/env python3

"""Collection of Utilities."""

import subprocess
import requests


def shell(*args):
    """Execute shell commands and return stdout."""
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    stdout, out = process.communicate()
    return stdout


def python_gitignore():
    """Pull latest Python.gitignore file from github."""
    URL = 'https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore'
    r = requests.get(URL)
    with open('Python.gitignore', 'wb') as f:
        f.write(r.content)
