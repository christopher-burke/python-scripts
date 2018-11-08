#!/usr/bin/env python3

"""List file type info."""

from pathlib import Path
import fleep
import json
import argparse


class FileInquisitor:

    def f(self, p):
        for x in p.glob('*'):
            if x.is_file():
                with open(x, "rb") as file:
                    info = fleep.get(file.read(128))
                    r = json.dumps(info.__dict__)
                    print(x.name, r)
            if x.is_dir():
                self.f(Path(x))


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                     description='List file info.')
    parser.add_argument('src_dir', type=str, help='source directory')
    args = parser.parse_args()
    DRIVE = args.src_dir
    p = Path(DRIVE)
    fi = FileInquisitor()
    fi.f(p)


main()
if __name__ == "__main__":
    main()
