#!/usr/bin/env python3

# Copyright (C) 2013-2014 Jai Luthra <me@jailuthra.in>
# See LICENSE file for more details

'''Encrypt or Decrypt data using One-Time Pad'''

import binascii, argparse, itertools

def main():
    parser = argparse.ArgumentParser(
            description='Encrypt or Decrypt data using One-Time Pad')
    parser.add_argument('-d', '--decrypt', action='store_true',
            help='Decrypt data (default is to encrypt)')
    parser.add_argument('-f', '--file', dest='filename',
            help='File name to encrypt/decrypt')
    args = parser.parse_args()
    fname = args.filename
    # Decrypt Mode
    if args.decrypt:
        if fname == None:
            cipher = input('Cipher: ')
            key = input('Key: ')
            print('Message:', decrypt(cipher, key))
        else: # Read from a file
            with open(fname, 'r') as cryptfile:
                key = input('Key: ')
                cipher = cryptfile.read()
                print(decrypt(cipher, key))
    # Encrypt Mode (default)
    else:
        if fname == None:
            msg = input('Message: ')
            key = input('Key: ')
            if len(key) < len(msg):
                print('\nWARNING: Key size less than the message is unsafe')
            print('Cipher:', encrypt(msg, key))
        else: # Write to a file
            with open(fname, 'r') as f:
                key = input('Key: ')
                msg = f.read()
                if len(key) < len(msg):
                    print('\nWARNING: Key size less than the message is unsafe')
                cryptfile = open(fname + '.otpp', 'w')
                cryptfile.write(encrypt(msg, key))
                cryptfile.close()
                print('Encrypted data has been written to', fname+'.otpp')

def encrypt(msg, key):
    '''Return cipher text'''
    cipher = xor_str(msg, key)
    # ascii armor the cipher text
    cipher = (binascii.hexlify(cipher.encode())).decode()
    return cipher

def decrypt(cipher, key):
    '''Return plain text message'''
    # get back the string from ascii armored cipher
    cipher = (binascii.unhexlify(cipher.encode())).decode()
    msg = xor_str(cipher, key)
    return msg

def xor_str(a, b):
    '''Return the xor of the two strings a and b
    The length of the output string is the same as that of first string,
    which means that if second string is shorter than first, it'll be repeated
    over.'''
    xorred = ''.join([chr(ord(x)^ord(y)) for x, y in zip(a, itertools.cycle(b))])
    return xorred

if __name__ == "__main__":
    main()
