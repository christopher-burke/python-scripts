#!/usr/bin/env python3

"""Rotational Cipher."""

import sys
import logging

logging.basicConfig(level=logging.DEBUG)

plain = "abcdefghijklmnopqrstuvwxyz"


def create_plain():
    """Create string of plain characters alphabetized."""
    return "abcdefghijklmnopqrstuvwxyz"


def create_cipher(key):
    """Determine the cipher from the key."""
    if key > 26 or key < 0:
        raise ValueError("Please enter a vaild key: 0 <= key >= 26.")
    return plain[key:] + plain[:key]


def letter_index(i):
    """Find the letter index in the plain string."""
    try:
        index = plain.index(i.lower())
    except (IndexError, ValueError):
        return i
    return index


def apply_cipher(input_str, cipher):
    """Apply cipher to an input string."""
    cipher_text = ''
    for ltr in input_str:
        if ltr.isupper():
            case = str.upper
        else:
            case = str.lower

        index = letter_index(ltr)

        try:
            cipher_text += case(cipher[index])
        except (ValueError, TypeError):
            cipher_text += ltr
    return cipher_text


if __name__ == "__main__":
    try:
        key = int(sys.argv[1])
    except TypeError:
        print("Enter a numeric key.")

    input_str = sys.argv[2]

    cipher = create_cipher(key)
    print(apply_cipher(input_str, cipher))

    try:
        if sys.argv[3]:
            logging.debug('Running tests.')
            assert apply_cipher('omg', create_cipher(5)) == 'trl'
            assert apply_cipher('AbC', create_cipher(0)) == 'AbC'
            assert apply_cipher('Awesome', create_cipher(26)) == 'Awesome'
            assert apply_cipher('Pack my box with five dozen liquor jugs.', create_cipher(13)) == 'Cnpx zl obk jvgu svir qbmra yvdhbe whtf.'
            assert apply_cipher('Cnpx zl obk jvgu svir qbmra yvdhbe whtf.', create_cipher(13)) == 'Pack my box with five dozen liquor jugs.'
            logging.debug("Pass")
    except IndexError:
        pass
