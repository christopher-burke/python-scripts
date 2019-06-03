#!/usr/bin/env python3

"""Bored - Suggest an activity with boredapi.com."""

import json
from contextlib import closing
from urllib.request import urlopen


BOREDAPI_URL = "https://www.boredapi.com/api/activity/"


class Activity:
    """Activity Class."""

    def __init__(self, *args, **kwargs):
        """Create an Activity object with boredapi.com json response."""
        self.__dict__.update(kwargs)


def random_activity() -> str:
    """Get random activity."""
    action = closing(urlopen(BOREDAPI_URL))
    with action as response:
        output = response.read().decode('utf-8')
    return output


def parse_activity(json_response) -> str:
    """Get the activity from the JSON response."""
    boredapi_json_activity = json.loads(json_response)
    act = Activity(**boredapi_json_activity)
    return act.activity


def get_activity():
    """Get activity from boredapi.com."""
    json_response = random_activity()
    activity = parse_activity(json_response=json_response)
    return activity


def main():
    """Run get_activity function. Main Method do not import."""
    print(f"{get_activity()}.")


if __name__ == "__main__":
    main()
