#!/usr/bin/env python3

"""Bingo card generator.

    The Bingo balls letters and numbers:
        * "B" (numbers 1–15)
        * "I" (numbers 16–30)
        * "N" (numbers 31–45)
        * "G" (numbers 46–60)
        * "O" (numbers 61–75)
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors

from itertools import permutations, combinations
from pprint import pprint
from random import choice
from bingo_caller import bingo_ball, bingo_balls

def free_space(t : tuple):
    l = list(t)
    l.insert(2, 'FREE SPACE')
    t = tuple(l)
    return t

if __name__ == "__main__":
    balls = [ball for ball in bingo_balls()]
    b_balls = [b for b in balls if b.letter is 'B']
    i_balls = [b for b in balls if b.letter is 'I']
    n_balls = [b for b in balls if b.letter is 'N']
    g_balls = [b for b in balls if b.letter is 'G']
    o_balls = [b for b in balls if b.letter is 'O']

    b_columns = list(permutations(b_balls, 5))
    i_columns = list(permutations(i_balls, 5))
    n_columns = list(permutations(n_balls, 4))
    g_columns = list(permutations(g_balls, 5))
    o_columns = list(permutations(o_balls, 5))

    hashes = []
    cards = []

    for i in range(0,200):
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
