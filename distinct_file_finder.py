#!/usr/bin/env python3

"""Distinct Files in directory.

Find distinct files in a directory, then copy
those distinct files to a new directory.
"""

from shutil import copyfile
import sys
import pathlib
import hashlib


def search(d):
    """Search directory for files."""
    p = pathlib.Path(d)
    print(f"Searching {p.as_posix()}")
    directories = [dir_ for dir_ in p.iterdir() if dir_.is_dir()]
    files = [file_.as_posix() for file_ in p.iterdir()
             if file_.is_file()]
    for dir_ in directories:
        files.extend(search(dir_))
    return files


def md5(file_name):
    """Create MD5 Hash."""
    md5 = hashlib.md5(open(file_name, 'rb').read()).hexdigest()
    return md5


def sha256(file_name):
    """Create SHA256 Hash."""
    sha256 = hashlib.sha256(open(file_name, 'rb').read()).hexdigest()
    return sha256


def hasher(file_name):
    """Hashing function.

    Change this to the hashing algorithm of choice.
    md5
    sha256
    """
    return sha256(file_name)


def main():
    """Process the files in the directories."""
    t = sys.argv[1]
    p = pathlib.Path(t)
    root = p.as_posix()

    files = search(p)

    distinct = {}
    for file_ in files:
        hash = hasher(file_)
        if not distinct.get(hash, None):
            distinct[hash] = file_

    print(f"Found {len(distinct)} distinct files. ",
          "Copying files to distinct dir.")

    for k, v in distinct.items():
        path, _, filename = v.rpartition('/')
        distinct = path.partition(root)[-1]
        new_distinct_dir = root + '/distinct' + distinct

        pathlib.Path(new_distinct_dir).mkdir(parents=True, exist_ok=True)
        copyfile(v, new_distinct_dir + '/' + filename)


if __name__ == "__main__":
    main()
