#!/usr/bin/python
from collections import OrderedDict
import sys
import re
import string

def create_key(key):
    tmp = (key + string.ascii_uppercase).replace('J', '')
    return ''.join(OrderedDict.fromkeys(tmp))

def prepare_input(plaintext):
    tuples = []
    i = 0
    while (i < len(plaintext)):
        bigram = list(plaintext[i:i+2])

        if len(bigram) < 2:
            bigram.append('Z')
        if bigram[0] == bigram[1]:
            bigram[1] = 'Z'
            i += 1
        else:
            i += 2
        tuples.append(bigram)
    return tuples

def find_pos(char, key):
    x = key.find(char) % 5
    y = key.find(char) // 5
    return [x,y]

def find_char(pos, key):
    return key[pos[0] + pos[1]*5];

def encrypt(plaintext, key):
    key = create_key(key)
    print (key)
    tuples = prepare_input(plaintext)
    # print(tuples)

    ciphertext = []

    for elmt in tuples:
        pos0 = find_pos(elmt[0], key)
        pos1 = find_pos(elmt[1], key)
        newpos0 = list(pos0)
        newpos1 = list(pos1)
        # print (elmt, pos0, pos1)
        if (pos0[0] == pos1[0]): # sama kolomnya, turun 1
            newpos0[1] = (pos0[1] + 1) % 5
            newpos1[1] = (pos1[1] + 1) % 5
            # print(newpos0, newpos1)
        elif (pos0[1] == pos1[1]): # sama baris, ambil sebelah kanan
            newpos0[0] = (pos0[0] + 1) % 5
            newpos1[0] = (pos1[0] + 1) % 5
            # print(newpos0, newpos1)
        else:
            # print ("h")
            newpos0[0] = pos1[0]
            newpos1[0] = pos0[0]

        cipher_bigram = find_char(newpos0, key) + find_char(newpos1, key)
        # print(newpos0, newpos1, cipher_bigram)
        ciphertext.append(cipher_bigram)
        # print()

    # print (ciphertext)
    return ''.join(ciphertext)

def decrypt(ciphertext, key):
    key = create_key(key)
    print (key)
    tuples = prepare_input(ciphertext)
    print(tuples)

    ciphertext = []

    for elmt in tuples:
        pos0 = find_pos(elmt[0], key)
        pos1 = find_pos(elmt[1], key)
        newpos0 = list(pos0)
        newpos1 = list(pos1)
        # print (elmt, pos0, pos1)
        if (pos0[0] == pos1[0]): # sama kolomnya, turun 1
            newpos0[1] = (pos0[1] - 1) % 5
            newpos1[1] = (pos1[1] - 1) % 5
            # print(newpos0, newpos1)
        elif (pos0[1] == pos1[1]): # sama baris, ambil sebelah kanan
            newpos0[0] = (pos0[0] - 1) % 5
            newpos1[0] = (pos1[0] - 1) % 5
            # print(newpos0, newpos1)
        else:
            # print ("h")
            newpos0[0] = pos1[0]
            newpos1[0] = pos0[0]

        cipher_bigram = find_char(newpos0, key) + find_char(newpos1, key)
        # print(newpos0, newpos1, cipher_bigram)
        ciphertext.append(cipher_bigram)
        # print()

    # print (ciphertext)
    return ''.join(ciphertext)
