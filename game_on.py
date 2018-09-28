#!/usr/bin/env python3

"""Game on.

Games won tracker.
"""


from dataclasses import dataclass, asdict
import json
import sys
# from datetime import date


@dataclass
class Player:
    """Player dataclass."""

    name: str


@dataclass
class Match:
    """Match dataclass."""

    game: str
    date: date = date.today().__str__()


@dataclass
class Results:
    """Results dataclass."""

    match: Match
    player: Player
    wins: int = 0
    losses: int = 0


def load():
    """Load data from json file."""
    with open('game_on.json') as json_file:
        data = json.load(json_file)

    return data


def write(data, *args, **kwargs):
    """Write data to the json file."""
    with open('game_on.json', 'w') as json_file:
        json.dump(data, json_file)
    return True


def main():
    """Game on main funtion."""
    pass


if __name__ == "__main__":
    if not len(sys.argv) < 1:
        exit(0)

    match = Match('Name')  # -g "Name"
    p1 = Player('Player 1')  # -p1 "Name"
    p2 = Player('Player 2')  # -p1 "Name"
    r1 = Results(match, p1, 2)  # -r1 2
    r2 = Results(match, p2, 12)  # -r2 2

    r1.losses = r2.wins
    r2.losses = r1.wins

    data = {}

    data['result'] = [asdict(r1), asdict(r2)]
