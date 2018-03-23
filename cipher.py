#!/usr/bin/env python3

"""Cipher for encryption/decryption."""

from Crypto.Cipher import ARC4


class SimpleCipher:
    """Simple Cipher Example using Crypto's ARC4 Cipher."""

    def encrypt(self, text, key):
        """Encrypt text with key using Crypto.Cipher.ARC4."""
        ARC4_ = ARC4.new(key)
        cipher_text = ARC4_.encrypt(text)
        return cipher_text

    def decrypt(self, cipher_text, key):
        """Decrypt cipher_text with key using Crypto.Cipher.ARC4."""
        ARC4_ = ARC4.new(key)
        text = ARC4_.decrypt(cipher_text)
        return text


if __name__ == "__main__":
    sc = SimpleCipher()
    text = 'This is a sample text input.'
    key = '01234567'
    cipher_text = sc.encrypt(text=text, key=key)
    dec_text = sc.decrypt(cipher_text=cipher_text, key=key)

    print('Sample of SimpleCipher')
    print()
    print(f'Text = {text}')
    print(f'Key = {key}')
    print(f'cipher_text = {cipher_text}')
    print(f'dec_text = {dec_text}')
