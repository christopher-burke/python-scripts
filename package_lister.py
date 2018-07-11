#!/usr/bin/env python3


"""Package lister."""

import sys
import pathlib
import re
from collections import Counter


def find_imports(file_content: str, distinct: bool) -> set:
    """Find the imports in python file.

    Search the `import ..` and `from .. import ..` for package names.
    """
    IMPORT_REGEX = r'^[\s]*(?:import|(?P<type>from))\s+(?P<module>\w*)(?(type)\s+import\s+(?:.*)|(?:.*))$'
    imports = re.findall(IMPORT_REGEX, file_content, re.I | re.M)
    imports = [_[1] for _ in imports]
    if distinct:
        return set(imports)
    else:
        return imports


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


def package_collection(distinct: bool):
    """Return the package collection, set or list."""
    if distinct:
        package = set()
    else:
        package = []
    return package


def print_results(x):
    """Print results."""
    print(x)


def main(directory: str, distinct: bool):
    """Find all packages and print to console."""
    packages = package_collection(distinct)
    for path in search_dir(directory):
        if path.as_posix().rpartition('.')[-1] == 'py':
            with open(path.as_posix(), 'r') as f:
                file_content = "".join(f.readlines())
            if distinct:
                packages = packages | find_imports(file_content, distinct)
            else:
                packages.extend(find_imports(file_content, distinct))
    print_results(sorted(packages, key=lambda x: x.lower()))
    print_results(Counter(packages).most_common())


if __name__ == "__main__":
    directory = sys.argv[1]
    distinct = True
    main(directory, distinct)
