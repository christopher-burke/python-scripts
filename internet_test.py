#!/usr/bin/env python3

"""Internet working.

Using the nc command on macOS, test if the internet is working.

Google Public DNS = 8.8.8.8
"""


from subprocess import call, DEVNULL


def main(host: str, port: int) -> bool:
    """Test if the internet is working.

    :param host: hostname or ip address to nc.
    :param port: TCP port.
    :return: True or False.
    """
    command = ('nc', host, str(port), '-zv',)
    return call(command, stderr=DEVNULL, stdout=DEVNULL) == 0


if __name__ == "__main__":
    print(main(host='8.8.8.8', port=53))
