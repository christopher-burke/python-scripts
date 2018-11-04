#!/usr/bin/env python3


"""External IP - using requests, get the extrenal IP Address."""

import requests
import re

IP_ADDRESS_REGEX = r'((?:\d{1,3}\.){3}\d{1,3})'


def external_ip(site):
    """Get the external IP address."""
    r = requests.get(site)
    if r.status_code == 200:
        ip_address = re.findall(IP_ADDRESS_REGEX, r.text, re.I | re.M)[0]
    else:
        raise ValueError(f"A status code pf {r.status_code} was returned.")

    return ip_address


def main():
    """Run the External IP script."""
    site = 'https://www.privateinternetaccess.com/pages/whats-my-ip/'
    return external_ip(site)


if __name__ == "__main__":
    print(main())
