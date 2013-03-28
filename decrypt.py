#!/usr/bin/env python2

# Copyright (C) 2013 Jai Luthra <me@jailuthra.in> 

cipher = raw_input('\nEnter the cipher text you want to decrypt: ').decode("hex")
msg = ''
key = raw_input('Enter the password earlier used in encryption: ')
i = 0
j = 0
for i in range( len(cipher) ):
    c = ord(cipher[i])
    k = ord(key[j])
    m = c^k
    msg += chr(m)
    j += 1
    if ( j==len(key) ):
        j=0
           
print ('The original message is: '+ msg)

  
