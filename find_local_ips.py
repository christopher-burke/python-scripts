#!/usr/bin/env python3

"""Find all local ip addresses in an ip network."""

import ipaddress
import socket


# Set up
HOSTNAME = socket.gethostname()
HOSTIP = socket.gethostbyname(HOSTNAME)
NETWORK = ipaddress.ip_network(f'{HOSTIP}/24', strict=False)
NONACTIVE = []

# Print Non-Active IPs
PRINT_NON_ACTIVE_IPS = False


def main():
    """Show all hostnames and ip address on local network."""
    for ip in NETWORK:
        address = str(ip)
        try:
            REMOTE_HOST = socket.gethostbyaddr(address)
            print(f'{REMOTE_HOST[0]} at {REMOTE_HOST[2][0]}.')
        except socket.herror as e:
            NONACTIVE.append(address)
    if PRINT_NON_ACTIVE_IPS:
        print(", ".join(NONACTIVE))


if __name__ == "__main__":
    main()
