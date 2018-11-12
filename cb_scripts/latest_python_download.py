#!/usr/bin/env python3

"""Download latest Python from FTP site."""

import sys
from latest_python_FTP_version import latest
from urllib.request import urlretrieve, urlopen


def get_python(filename, url):
    """Download the latest python version."""
    request = urlopen(f'{url}/{filename}', timeout=500)

    with open(f'{filename}', 'wb') as f:
        try:
            f.write(request.read())
        except:
            print("error")


def ftp_urls():
    """Get the latest version of python from python.org."""
    latest_version = latest(url='https://www.python.org/ftp/python/')
    ftp_url_base = f'https://www.python.org/ftp/python/{latest_version}/'
    zip_file = f'Python-{latest_version}.tgz'
    return (ftp_url_base, zip_file)


def main():
    try:
        ftp_url_base, zip_file = ftp_urls()
        get_python(zip_file, ftp_url_base)
    except:
        sys.exit(1)
    return 0


if __name__ == "__main__":
    print(main())
