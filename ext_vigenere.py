#!/usr/bin/python
import sys
import re
import string


def encrypt(plaintext, key):
    ciphertext = []
    key_length = len(key)
    for i in range(len(plaintext)):
        p = plaintext[i]
        k = ord(key[i % key_length])
        c = (p + k) % 256
        ciphertext.append(c)
    return bytes(ciphertext)

def decrypt(ciphertext, key):
    plaintext = []
    key_length = len(key)
    for i in range(len(ciphertext)):
        p = ciphertext[i]
        k = ord(key[i % key_length])
        c = (p - k) % 256
        plaintext.append(c)
    return bytes(plaintext)
