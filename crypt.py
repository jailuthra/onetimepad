#!/usr/bin/env python

# Copyright (C) 2013 Jai Luthra <me@jailuthra.in> 

repeat='y'
print ('=======ENCRYPTER=======\n\n')
while repeat!='n':
    str1=raw_input('\nEnter the string you want to crypt: ')
    str2=''
    k=raw_input('Enter the password: ')
    i=0
    j=0
    for i in range(len(str1)):
        x=ord(str1[i])
        y=ord(k[j])
        
        """if (x<123 and x>96):
            x=x-96
            y=y-96
            if((x+y)%26==0):
                x=x+y
            else:
                x=(x+y)%26
            x=x+96
            y=y+96
            
        elif (x<91 and x>64):
            x=x-64
            y=y-96
            if((x+y)%26==0):
                x=x+y
            else:
                x=(x+y)%26
            x=x+64
            y=y+96"""
        
        x=x-32
        y=y-32
        x=(x+y)%(126-32+1)
        x=x+32
                     
        str2=str2+chr(x)
        j=j+1
        if (j==len(k)):
            j=0
        
            
    print ('Your Required String Is: '+str2)
    repeat=raw_input('Do It Again? ')
    print ('\n\n')

  
