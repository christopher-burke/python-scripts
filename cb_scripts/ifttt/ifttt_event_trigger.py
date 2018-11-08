#!/usr/bin/env python3

"""IFTTT Maker Webhooks event trigger."""

import os
import requests

# Get the IFTTT key and event name from environment variables.
# Set this variables in your virtualenv startup or .bashrc profile.
IFTTT_KEY = os.environ.get('IFTTT_TOKEN')
IFTTT_EVENT = os.environ.get('IFTTT_EVENT')

# IFTTT url format using f strings.
IFTTT_URL = f'https://maker.ifttt.com/trigger/{IFTTT_EVENT}/with/key/{IFTTT_KEY}'


def post_ifttt(value):
    """Post value IFTTT trigger."""
    data = {'value1': value}
    requests.post(IFTTT_URL, json=data)


if __name__ == "__main__":
    value = 'Hello World!'
    post_ifttt(value)
