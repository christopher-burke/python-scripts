#!/usr/bin/env python3

"""Five O'clock Whistle."""

import sys
import webbrowser
from datetime import datetime


def main():
    while True:
        now = datetime.now().strftime("%I:%M %p")
        if now == '05:00 PM':
            webbrowser.open('https://www.youtube.com/watch?v=oCnRV3SQkKk')
            sys.exit(0)


if __name__ == "__main__":
    main()
