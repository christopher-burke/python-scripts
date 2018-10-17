#!/usr/bin/env python3

"""Reckon - simple substitution cipher."""

import os
from base64 import b64decode, b64encode
from string import ascii_letters, punctuation, digits
from hashlib import sha512


chars = tuple(ch for ch in (*ascii_letters, *punctuation, *digits, ' ',))


def hash_() -> str:
    """Create has from environment var RECKON_KEY."""
    KEY = os.getenv('RECKON_KEY', default='SECRET_KEY')
    return sha512(KEY.encode()).hexdigest()


def mapping(hash_string: str) -> dict:
    """Create mapping for the substitution cipher."""
    cipher = list(chars)
    for c in hash_string:
        char_int = int(c, 16)
        pos = len(cipher) * (char_int / 15)
        cipher.insert(0, cipher.pop(int(pos)-1))
        cipher = cipher[::-1]

    mapping_ = dict()

    for index, char_ in enumerate(chars):
        mapping_[char_] = cipher[index]

    return mapping_


def convert_string(string: str, type: str) -> str:
    """Convert the string by [e]ncrypting or [d]ecrypting.

    :param type: String 'e' for encrypt or 'd' for decrypt.
    :return: [en/de]crypted string.
    """
    hash_string = hash_()
    map_ = mapping(hash_string)

    if type.lower() == 'e':
        output = encrypt(string, map_)
    elif type.lower() == 'd':
        map_ = {v: k for k, v in map_.items()}
        output = decrypt(string, map_)
    else:
        output = ''
    return output


def encrypt(string: str, map_: dict) -> str:
    """Encrypt the string using map_.

    :return: Encrypted string
    """
    encrypted = []
    for index, char_ in enumerate(string):
        encrypted.append(map_[char_])

    return ''.join(encrypted)


def decrypt(string: str, map_: dict) -> str:
    """Decrypt the string using map_.

    :return: Decrypted string
    """
    decrypted = []
    for index, char_ in enumerate(string):
        decrypted.append(map_[char_])

    return ''.join(decrypted)


def main():
    """Sample encryption decryption."""
    in_str = 'This is a test string for the cipher.'
    in_str = b64encode(in_str.encode()).decode()
    in_str = convert_string(in_str, 'e')
    print(in_str)
    out_str = """t$wmik7mik7wu;h8i{g^i{hk=AWyu$"?if7B=$r^OX8s=$tkQ^HH"""
    out_str = convert_string(out_str, 'd')
    print(b64decode(out_str).decode())
    print(len(in_str))


if __name__ == "__main__":
    main()
