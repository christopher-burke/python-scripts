#!/usr/bin/env python3

"""List Virtual Environment Python versions."""


import os
from pathlib import Path
from subprocess import Popen, PIPE


def main():
    """Print virtualenv and python version."""
    workon_home = os.environ.get('WORKON_HOME')
    workon_home = Path(workon_home)

    for virtualenv in workon_home.iterdir():
        if virtualenv.is_dir():
            for python_bin in Path(f'{virtualenv}/bin/').iterdir():
                if python_bin.name == 'python':
                    command = [f'{python_bin}',
                               '-c',
                               "import sys;print(sys.version.split()[0]);"
                               ]
                    stdout, _ = Popen(command, stdout=PIPE).communicate()
                    stdout = stdout.decode('utf-8')
                    print(f'{python_bin} uses Python {stdout.strip()}.')


if __name__ == "__main__":
    main()
