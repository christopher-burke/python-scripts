#!/usr/bin/env python3

"""Arrange Files - File organizer."""

import os
import sys
import shutil
import uuid


mapping = {
    'images': ['ai', 'bmp', 'gif', 'ico', 'jpeg', 'jpg', 'pbm', 'png',
               'pnm', 'ps', 'psd', 'svg', 'tif', 'tiff'],
    'music': ["wav", "mp3", "flac", "3gp", "aa", "aax", "aiff", "raw"],
    'executables': ["exe", "tar", "deb", ],
    'documents': ['doc', 'docx', 'md', 'odt', 'pdf', 'ppt', 'pptx',
                  'rtf', 'tex', 'txt', 'wks', 'wpd', 'wps', 'xls', 'xlsx'],
    'videos': ['3g2', '3gp', 'avi', 'flv', 'h264', 'm4v', 'mkv', 'mov',
               'mp4', 'mpeg', 'mpg', 'rm', 'swf', 'vob', 'webm', 'wmv'],
    'disc_images': ["bin", "dmg", "iso", "toast", "vcd", ],
    'data': ['xml', 'csv', 'db', 'dat', ],
    'compressed': ['7z', 'arj', 'deb', 'pkg', 'rar', 'rpm', 'tar', 'gz',
                   'z', 'zip', ]
}


def main(dir_path, delete=False):
    """Arrange files based on mapping."""
    os.chdir(dir_path)
    for filename in os.listdir(dir_path):
        name, delim, extension = filename.rpartition('.')
        for k, v in mapping.items():
            if extension.lower() in v:
                if not os.path.exists(f"{k}"):
                    os.makedirs(f"{k}")
                if os.path.exists(f'{k}/{filename}'):
                    duplicate_filename = f'{filename}{uuid.uuid4().hex}'
                    shutil.copy(filename, duplicate_filename)
                    shutil.copy2(duplicate_filename, f'{k}')
                    print(f'moved {duplicate_filename} to {k}')
                    if delete:
                        os.remove(duplicate_filename)
                else:
                    shutil.copy2(filename, f'{k}')
                    print(f'moved {filename} to {k}')
                if delete and os.path.exists(f'{k}/{filename}'):
                    os.remove(filename)


if __name__ == "__main__":
    start_dir = os.curdir
    dir_path = sys.argv[1]
    main(dir_path=dir_path)
    os.chdir(start_dir)
