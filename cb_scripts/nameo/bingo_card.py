#!/usr/bin/env python3

"""Bingo card generator.

    The Bingo balls letters and numbers:
        * "B" (numbers 1–15)
        * "I" (numbers 16–30)
        * "N" (numbers 31–45)
        * "G" (numbers 46–60)
        * "O" (numbers 61–75)
"""

from itertools import permutations
from pprint import pprint
from random import choice
from ball import bingo_balls
from jinja2 import Environment, FileSystemLoader


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('base.html')


def free_space(column: tuple) -> tuple:
    """Add Bingo FREE space."""
    column = list(column)
    column.insert(2, 'FREE SPACE')
    column = tuple(column)
    return column


if __name__ == "__main__":
    balls = [ball for ball in bingo_balls()]
    b_balls = [b for b in balls if b.letter is 'B']
    i_balls = [i for i in balls if i.letter is 'I']
    n_balls = [n for n in balls if n.letter is 'N']
    g_balls = [g for g in balls if g.letter is 'G']
    o_balls = [o for o in balls if o.letter is 'O']

    b_columns = list(permutations(b_balls, 5))
    i_columns = list(permutations(i_balls, 5))
    n_columns = list(permutations(n_balls, 4))
    g_columns = list(permutations(g_balls, 5))
    o_columns = list(permutations(o_balls, 5))

    hashes = []
    cards = []

    for i in range(0, 200):
        card = (choice(b_columns),
                choice(i_columns),
                free_space(choice(n_columns)),
                choice(g_columns),
                choice(o_columns),
                )
        card_hash = hash(card)
        if card_hash in hashes:
            pprint("Card Created already.")
        else:
            hashes.append(card_hash)
            cards.append([e for t in card for e in t])

    with open(f'bingo-card.html', 'a') as f:
        f.write(template.render(cards=cards))
