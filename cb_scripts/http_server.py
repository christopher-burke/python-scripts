#!/usr/bin/env python3

"""Python Http server ("Hello, World!").

Fun with sockets and multiprocessing.

source: https://www.youtube.com/watch?v=MRToT6vVfQE
"""

import socket
import multiprocessing


def handle(connection, client_address):
    """Handle the connection."""
    print('handling', client_address)
    connection.send(b'HTTP/1.1 200 OK\r\n')
    connection.send(b'Content-type: text/html\r\n')
    connection.send(b'Content-Length: 13\r\n')
    connection.send(b'\r\n')
    connection.send(b'Hello, World!\r\n\r\n')
    connection.close()


def main():
    """`Hello, World!` http server."""
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM)
    sock.bind(('', 8989,))
    sock.listen(1)

    while True:
        connection, client_address = sock.accept()
        print('new connection')
        process = multiprocessing.Process(target=handle,
                                          args=(connection, client_address))
        process.start()


if __name__ == "__main__":
    main()
