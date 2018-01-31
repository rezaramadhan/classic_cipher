#!/usr/bin/python3
import sys
import re
import vigenere
import ext_vigenere
import playfair

def process_vigenere(mode, input_text, key, output_type, output_file):
    if mode == "encrypt":
        print("Plaintext:\n----------------------------")
        print (input_text.decode('utf-8'))

        ciphertext = vigenere.encrypt(input_text.decode('utf-8'), key.upper())
        if output_type == "a":
            processed_ciphertext = ciphertext
        elif output_type == "b":
            processed_ciphertext = re.sub('\W', '', ciphertext)
        elif output_type == "c":
            ciphertext = re.sub('\W', '', ciphertext).upper()
            processed_ciphertext = ' '.join(ciphertext[i:i+5] for i in range(0,len(ciphertext),5))
        else:
            print ("Invalid output option")
            sys.exit(2)

        print ("Ciphertext:\n----------------------------")
        print (processed_ciphertext)

        open(output_file, 'w').write(processed_ciphertext)
    elif mode == "decrypt":
        print ("Ciphertext:\n----------------------------")
        print (input_data.decode('utf-8'))

        ciphertext = re.sub('\W', '', input_text).upper()
        plaintext = vigenere.decrypt(ciphertext, key.upper())

        print ("Plaintext:\n----------------------------")
        print (plaintext)

        open(output_file, 'w').write(plaintext)

def process_ext_vigenere(mode, input_text, key, output_type, output_file):
    if mode == "encrypt":
        print ("Plaintext:\n----------------------------")
        print (input_text)

        ciphertext = ext_vigenere.encrypt(input_text, key.upper())

        print ("Ciphertext:\n----------------------------")
        print (ciphertext)

        open(output_file, 'wb').write(ciphertext)
    elif mode == "decrypt":
        print ("Ciphertext:\n----------------------------")
        print (input_data)

        plaintext = ext_vigenere.decrypt(input_data, key.upper())

        print ("Plaintext:\n----------------------------")
        print (plaintext)

        open(output_file, 'wb').write(plaintext)

def process_playfair(mode, input_text, key, output_type, output_file):
    if mode == "encrypt":
        print ("Plaintext:\n----------------------------")
        print (input_text.decode('utf-8'))
        plaintext = input_text.decode('utf-8')

        plaintext = re.sub('\W', '', plaintext).upper().replace('J', 'I')
        ciphertext = playfair.encrypt(plaintext, key.replace(' ', '').upper())

        ciphertext = ' '.join(ciphertext[i:i+5] for i in range(0,len(ciphertext),5))
        print ("Ciphertext:\n----------------------------")
        print (ciphertext)

        open(output_file, 'w').write(ciphertext)
    elif mode == "decrypt":
        print ("Ciphertext:\n----------------------------")
        print (input_text.decode('utf-8'))

        ciphertext = re.sub('\W', '', input_text.decode('utf-8')).upper()
        plaintext = playfair.decrypt(ciphertext, key.replace(' ', '').upper())

        print ("Plaintext:\n----------------------------")
        print (plaintext)

        open(output_file, 'w').write(plaintext)

if __name__ == '__main__':
    if len(sys.argv) != 7:
        print ("Usage: ./dencryptor.py <vigenere|ext_vigenere|playfair> <ecrypt|decrypt> <input_file> <output_file> <key> <output_type>")
        sys.exit(1)

    input_data = open(sys.argv[3], 'rb').read()

    if (sys.argv[1] == "vigenere"):
        process_vigenere(sys.argv[2], input_data, sys.argv[5], sys.argv[6], sys.argv[4])
    elif(sys.argv[1] == "ext_vigenere"):
        process_ext_vigenere(sys.argv[2], input_data, sys.argv[5], sys.argv[6], sys.argv[4])
    elif(sys.argv[1] == "playfair"):
        process_playfair(sys.argv[2], input_data, sys.argv[5], sys.argv[6], sys.argv[4])
    else:
        print ("Invalid algorithm")
        exit(3)
