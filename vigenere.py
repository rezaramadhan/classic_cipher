#!/usr/bin/python
import sys
import re
import string

def encrypt(plaintext, key):
    ciphertext = []
    key_length = len(key)
    counter = 0
    for i in range(len(plaintext)):
        is_uppercase = False
        if plaintext[i] in string.ascii_letters:
            if (plaintext[i] in string.ascii_uppercase):
                is_uppercase = True
            p = ord(plaintext[i].lower()) - 97
            k = ord(key[counter % key_length]) - 65
            c = (p + k) % 26
            c = chr(c + 97)
            if (is_uppercase):
                c = c.upper()
            ciphertext.append(c)
            counter += 1
        else:
            ciphertext.append(plaintext[i])
    return ''.join(ciphertext)

def decrypt(ciphertext, key):
    plaintext = []
    key_length = len(key)
    for i in range(len(ciphertext)):
        p = ord(ciphertext[i]) - 65
        k = ord(key[i % key_length]) - 65
        c = (p - k) % 26
        c = chr(c + 65)
        plaintext.append(c)
    return ''.join(plaintext)
