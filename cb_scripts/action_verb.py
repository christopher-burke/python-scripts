#!/usr/bin/env python3

"""Action Verbs.

Pick a random action verb from data/action_verb.json.

"""

import random
import json
from pathlib import Path


def load(
    action_verb_json: str = 'data/json/action_verbs.json',
    key: str = 'ACTION_VERBS'
):
    """Load the action verbs."""
    BASE_DIR = Path(__file__).resolve().parent
    with open(f"{BASE_DIR}/{action_verb_json}", 'r') as raw_data:
        data = json.load(raw_data)
    return data['ACTION_VERBS']


def main():
    """Pick random action verb."""
    return random.choice(load())


action_verb = main

if __name__ == "__main__":
    print(main())
