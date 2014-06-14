#!/usr/bin/env python3

# Copyright (C) 2013-2014 Jai Luthra <me@jailuthra.in>

'''Decrypt an ascii-armored onetimepad cipher'''

import binascii

def main():
    cipher = input('Cipher: ')
    key = input('Key: ')
    msg = decrypt(cipher, key)
    print('Message:', msg)

def decrypt(cipher, key):
    '''Return plain text message'''
    i = 0
    j = 0
    msg = ''
    # get back the string from ascii armored cipher
    cipher = (binascii.unhexlify(cipher.encode('ascii'))).decode('ascii')
    for i in range(len(cipher)):
        c = ord(cipher[i])
        k = ord(key[j])
        m = c^k
        msg += chr(m)
        j += 1
        if j == len(key):
            j = 0
    return msg

if __name__ == "__main__":
    main()
