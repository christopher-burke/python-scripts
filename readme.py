#!/usr/bin/env python3

"""Generate the README.md file a repo."""

from pathlib import Path
import ast
from jinja2 import Environment, FileSystemLoader
from subprocess import Popen, PIPE

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('readme_template.md')

FILES = Popen("git ls-tree -r master --name-only",
              shell=True, stdout=PIPE).stdout.read()
FILES = FILES.decode().split('\n')
EXTENSION = '.py'
scripts = []


def get_value(value):
    """Get the first line of docstring, if None default return."""
    if value:
        return value.split('\n')[0]
    else:
        return None


def process(path, name):
    """Github Markdown table format for name and docstring."""
    d = {}
    global scripts
    with open(path.as_posix()) as fd:
        file_contents = fd.read()
    module = ast.parse(file_contents)
    docstring = ast.get_docstring(module)
    docstring_line = get_value(docstring)
    if docstring_line:
        d['name'] = name
        d['docstring'] = docstring_line
        scripts.append(d)


def search_dir(d, basepath, extension):
    """Search directories recursively for repo files."""
    for path in d.iterdir():
        string_path = str(path).replace(basepath, '')[1:]
        if path.is_dir():
            search_dir(path, basepath, extension)
        if string_path in FILES and path.suffix == extension:
            print(string_path)
            process(path, string_path)


def write_readme():
    """Write readme.md file."""
    global scripts
    with open('README.md', 'w') as f:
        f.write(template.render(scripts=scripts))


def main():
    """Create a readme.md file."""
    p = Path.cwd()
    search_dir(p, str(p), EXTENSION)
    write_readme()


if __name__ == "__main__":
    main()
