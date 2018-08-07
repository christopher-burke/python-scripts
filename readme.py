#!/usr/bin/env python3

"""Generate the README.md file a repo."""

from pathlib import Path, PosixPath
import ast
from jinja2 import Environment, FileSystemLoader
from subprocess import Popen, PIPE
from shlex import quote
from functools import partial


def load_template():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('readme_template.md')
    return template


def git_ls_tree(branch: str = 'master'):
    """Return the git ls-tree command."""
    branch = quote(branch)
    return f"git ls-tree -r {branch} --name-only"


def tracked_files():
    git_cmd = git_ls_tree()
    files = Popen(git_cmd,
                  shell=True,
                  stdout=PIPE).stdout.read()
    files = files.decode().split('\n')
    return files


def get_value(value):
    """Get the first line of docstring, if None default return."""
    if value:
        return value.split('\n')[0]
    else:
        return None


def process(path, name):
    """Github Markdown table format for name and docstring."""
    d = {}
    path = path / name
    with open(path.as_posix()) as fd:
        file_contents = fd.read()
    module = ast.parse(file_contents)
    docstring = ast.get_docstring(module)
    docstring_line = get_value(docstring)
    d['name'] = name
    if docstring_line:
        d['docstring'] = docstring_line
    else:
        d['docstring'] = 'No docstring provided.'
    return d


def search_dir(d: PosixPath, basepath, files, extension):
    """Search directories recursively for repo files."""
    scripts = []
    for path in d.iterdir():
        string_path = str(path).replace(basepath, '')[1:]
        if path.is_dir():
            recu_scripts = search_dir(path, basepath, files, extension)
            if recu_scripts:
                scripts.extend(recu_scripts)
        if string_path in files and path.suffix == extension:
            scripts.extend([string_path])
    return scripts


def write_readme(scripts):
    """Write readme.md file."""
    template = load_template()
    with open('README.md', 'w') as f:
        f.write(template.render(scripts=scripts))


def main():
    """Create a readme.md file."""
    p = Path.cwd()
    path = str(p)

    files = tracked_files()
    scripts = search_dir(p, path, files, '.py')
    scripts = list(map(partial(process, p), scripts))

    for script in scripts:
        script['display'] = script['name'].replace('_', '\_')
    write_readme(scripts)


if __name__ == "__main__":
    main()
