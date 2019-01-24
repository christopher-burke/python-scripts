#!/usr/bin/env python3

"""Rain. Tell if rain is in forecast."""


import requests
import os
import re


result_messages = {
    True: 'Rain in the forecast.',
    False: 'No rain.',
}


def rain(postal_code: str) -> bool:
    """Determine if rain is in forecast."""
    r = requests.get(f'https://weather.com/weather/hourbyhour/l/{postal_code}')
    rain_ = re.findall(
        r'(?:<span>.*)(Rain|Shower[s]?)(?:</span>)', r.text, re.I | re.M)
    return bool(rain_)


def main() -> str:
    """Print Rain or No Rain message."""
    postal_code = os.environ.get('POSTAL_CODE')
    rain_forecast = rain(postal_code=postal_code)
    return result_messages[rain_forecast]


if __name__ == "__main__":
    print(main())
