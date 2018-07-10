#!/usr/bin/env python3


"""Package lister."""

import sys
import pathlib
import re


def find_imports(file_content: str) -> set:
    """Find the imports in python file.

    Search the `import ..` and `from .. import ..` for package names.
    """
    IMPORT_REGEX = r'^[\s]*import (\w*)[\.\w]*$'
    FROM_REGEX = r'^[\s]*from (\w*)[\.\w]* import \w*[\.\w]*$'

    imports = re.findall(IMPORT_REGEX, file_content, re.I | re.M)
    from_imports = re.findall(FROM_REGEX, file_content, re.I | re.M)

    return set(imports + from_imports)


def search_dir(directory: str) -> str:
    """Recursively search directory."""
    p = pathlib.Path(directory)
    paths = []
    for path in p.iterdir():
        paths.append(path)
        if path.is_dir():
            paths.extend(search_dir(path))
    for path in paths:
        yield path


def main(directory: str):
    """Find all packages and print to console."""
    package_set = set()
    for path in search_dir(directory):
        if path.as_posix().rpartition('.')[-1] == 'py':
            with open(path.as_posix(), 'r') as f:
                file_content = "".join(f.readlines())
            package_set = package_set | find_imports(file_content)
    print(sorted(package_set, key=lambda x: x.lower()))


if __name__ == "__main__":
    directory = sys.argv[1]
    main(directory)
