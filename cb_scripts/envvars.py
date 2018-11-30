#!/usr/bin/env python3

"""Environment Variables.

Script to create a file with environment variables.
"""

import os


def main():
    """Create file with environment variables."""
    with open('envvars', 'w') as f:
        for key, value in os.environ.items():
            f.write(f'{key}={value}\n')


if __name__ == "__main__":
    main()
