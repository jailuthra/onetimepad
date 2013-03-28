#!/usr/bin/env python2

# Copyright (C) 2013 Jai Luthra <me@jailuthra.in> 

msg = raw_input('\nEnter the message you want to encrypt: ')
cipher = ''
key = raw_input('Enter the password to encrypt: ')
i = 0
j = 0
for i in range ( len(msg) ):
    m = ord(msg[i])
    k = ord(key[j])
    c = m^k
    cipher += chr(c).encode("hex")
    j += 1
    if ( j==len(key) ):
        j=0
                    
print ('The encrypted message is: '+ cipher)

  
