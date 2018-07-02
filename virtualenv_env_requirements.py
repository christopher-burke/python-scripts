#!/usr/bin/env python3

"""List Virtual Environment Python versions."""


import os
from pathlib import Path
from subprocess import Popen, PIPE
from jinja2 import Environment, FileSystemLoader


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('virtualenv_details.md')


def main():
    """Print virtualenv and python version."""
    workon_home = os.environ.get('WORKON_HOME')
    workon_home = Path(workon_home)

    for virtualenv in workon_home.iterdir():
        if virtualenv.is_dir():
            for python_bin in Path(f'{virtualenv}/bin/').iterdir():
                if python_bin.name == 'python':
                    virtual_environment = str(virtualenv).rpartition('/')[-1]
                    command = [f'{python_bin}',
                               '-c',
                               "import sys;print(sys.version.split()[0]);"
                               ]
                    stdout, _ = Popen(command, stdout=PIPE).communicate()
                    stdout = stdout.decode('utf-8')
                    python_version = stdout.strip()
                if python_bin.name == 'pip':
                    command = [f'{python_bin}',
                               'freeze'
                               ]
                    stdout, _ = Popen(command, stdout=PIPE).communicate()
                    stdout = stdout.decode('utf-8')
                    packages = [p.strip() for p in stdout.split()]
            with open(f'{os.uname()[1].split(".")[0]}.md', 'a') as f:
                f.write(template.render(virtualenv=virtual_environment,
                                        version=python_version,
                                        packages=packages))


if __name__ == "__main__":
    main()
