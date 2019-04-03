#!/usr/bin/env python3

"""Sort clipboard using subprocess module."""


import subprocess


def get_clipboard():
    """Get the clipboard from the pbpaste command."""
    paste = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    paste.wait()
    data = paste.stdout.read()
    return data.decode()


def set_clipboard(data):
    """Set the clipboard using the pbcopy command."""
    copy = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    copy.stdin.write(data)
    copy.stdin.close()
    return_code = copy.wait()
    return return_code


def sort(data):
    """Sort the data using builtin sorted function."""
    data_ = str(data).split('\n')
    data_ = sorted(data_)
    return str.encode('\n'.join(data_))


def main():
    """Run get_clipboard and set_clipboard."""
    data = get_clipboard()
    set_clipboard(sort(data))


if __name__ == "__main__":
    main()
