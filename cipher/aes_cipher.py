#!/usr/bin/env python3


"""AES encryption using PyCrypto."""

# padding module from PyCrypto:
# https://raw.githubusercontent.com/dlitz/pycrypto/master/lib/Crypto/Util/Padding.py

import os
from Crypto.Cipher import AES
from padding import pad, unpad
from Crypto import Random


class AESCipher:
    """AES Cipher."""

    def __init__(self, key, mode=None):
        """The AESCipher init method setting key and method.

        Requires key paramater.
        """
        self.key = key
        if mode:
            self.mode = mode
        else:
            self.mode = AES.MODE_CBC

    def encrypt(self, text):
        """Encrypt text."""
        text = pad(text.encode(), AES.block_size)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, self.mode, iv)
        return iv + cipher.encrypt(text)

    def decrypt(self, ciphertext):
        """Decrypt text."""
        iv = ciphertext[:16]
        ciphertext = ciphertext[16:]
        cipher = AES.new(self.key, self.mode, iv)
        plaintext = cipher.decrypt(ciphertext)
        return unpad(plaintext, AES.block_size).decode()


def b(x):
    """Byte helper function."""
    return eval(f"b'\\{x}'")


def key():
    """Get key from variables."""
    key = os.environ["KEY"]
    key = key.split("\\")
    key = b"".join([b(x) for x in key[1:]])
    return key


if __name__ == "__main__":
    key = key()
    cipher = AESCipher(key, mode=None)
    text = "This is a test!"
    ciphertext = cipher.encrypt(text)
    print(ciphertext)
    plaintext = cipher.decrypt(ciphertext)
    print(plaintext)
