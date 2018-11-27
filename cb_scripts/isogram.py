#!/usr/bin/env python3

"""Isogram - determine if a word is an isogram."""


def isogram(word):
    """Determine if word is isogram.

    :param: word - string.
    :return: True word is isogram and False otherwise.
    """
    word_list = [l for l in word.lower() if l.isalpha()]
    return len(set(word_list)) == len(word_list)
