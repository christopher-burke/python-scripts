#!/usr/bin/env python3

"""Location data based on External IP address."""

import requests
import json
from cb_scripts.external_ip import external_ip


def get_external_ip():
    """Return the external IP Address."""
    ip_address = external_ip(site="http://checkip.dyndns.com/")
    return ip_address


def get_location_data(ip_address):
    """Return the location data of ip_address."""
    location_data_url = f'http://ipinfo.io/{ip_address}/json'
    response = requests.get(location_data_url)
    data = response.json()
    return data


def main():
    """Print the Location data."""
    ip_address = get_external_ip()
    data = get_location_data(ip_address=ip_address)
    print(json.dumps(data, indent=4))


if __name__ == "__main__":
    main()
