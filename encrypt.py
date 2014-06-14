#!/usr/bin/env python3

# Copyright (C) 2013-2014 Jai Luthra <me@jailuthra.in>

'''Encrypt a text message into ascii-armored cipher text, using onetimepad'''

import binascii

def main():
    msg = input('Message: ')
    key = input('Key: ')
    if (len(key) < len(msg)):
        print('\nWARNING: It is insecure to have a key shorter than the message')
    cipher = encrypt(msg, key)
    print ('Cipher:', cipher)

def encrypt(msg, key):
    '''Return cipher text'''
    i = 0
    j = 0
    cipher = ''
    for i in range(len(msg)):
        m = ord(msg[i])
        k = ord(key[j])
        c = m^k
        cipher += chr(c)
        j += 1
        if j == len(key):
            j = 0
    # ascii armor the cipher text
    cipher = (binascii.hexlify(cipher.encode('ascii'))).decode('ascii')
    return cipher

if __name__ == "__main__":
    main()
