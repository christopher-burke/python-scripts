#!/usr/bin/env python3

"""Ping Scan"""

from subprocess import Popen, PIPE


def ping_scan(ip_address):
    """Ping the ip address and check for response."""
    p = Popen(['ping', '-c 1', ip_address],
              stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate(input=None)
    success_text = b"1 packets transmitted, 1 packets received"
    if success_text in stdout:
        return f'{ip_address} - replied.'


def main():
    """Run ping_scan on localhost."""
    results = ping_scan('localhost')
    if results:
        print(results)


if __name__ == "__main__":
    main()
