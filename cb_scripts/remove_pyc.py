#!/usr/bin/env python3

"""Search and remove pyc files."""

from pathlib import Path
import argparse


class RemovePyc:
    """Class to recursively search for pyc files."""

    def f(self, path):
        """Search for pyc files and delete them."""
        for x in path.glob('*'):
            if x.is_file():
                if any(x.suffix == y for y in ['pyc', '.pyc']):
                    print(x)
            if x.is_dir():
                self.f(Path(x))


def main():
    """Get the source directory, search and remove pyc files."""
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                     description='List file info.')
    parser.add_argument('src_dir', type=str, help='source directory')
    args = parser.parse_args()
    src_dir = args.src_dir
    p = Path(src_dir)
    pyc = RemovePyc()
    pyc.f(p)


if __name__ == "__main__":
    main()
