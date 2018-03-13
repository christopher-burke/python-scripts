#!/usr/bin/env python3

"""Generate the README.md file a repo."""

from pathlib import Path
import ast
from jinja2 import Environment, FileSystemLoader


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('readme_template.md')


def get_value(value):
    """Get the first line of docstring, if None default return."""
    if value:
        return value.split('\n')[0]
    else:
        return "Nothing defined."


def main():
    """Create a readme.md file."""
    with open('README.md', 'w') as f:
        p = Path.cwd()
        l = []
        for path in p.iterdir():
            d = {}
            if path.suffix == '.py':
                d['name'] = str(path.name)
                with open(path.as_posix()) as fd:
                    file_contents = fd.read()
                module = ast.parse(file_contents)
                docstring = ast.get_docstring(module)
                d['docstring'] = get_value(docstring)
                l.append(d)
        f.write(template.render(scripts=l))


if __name__ == "__main__":
    main()
