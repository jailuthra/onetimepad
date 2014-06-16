One-Time-Pad Python
===================

**One-Time-Pad Python is a command-line encryption tool**, which uses an encryption mechanism
very similar to [One-time Pad](https://en.wikipedia.org/wiki/One-time_pad) (Duh. Thanks for telling that)

Features
--------

* It can be used as a python script, or can be imported as a module.
* You can encrypt/decrypt data not only from stdin, but from a file too.
* It is Open Source! :D

Installation
------------

1. Clone it:  
```$ git clone https://github.com/jailuthra/onetimepad.git```
2. cd to the onetimepad directory:
```$ cd onetimepad/```
3. Run it:
```
$ ./otp.py -h
usage: otp.py [-h] [-d] [-f FILENAME]

Encrypt or Decrypt data using One-Time Pad

optional arguments:
  -h, --help            show this help message and exit
  -d, --decrypt         Decrypt data (default is to encrypt)
  -f FILENAME, --file FILENAME
                        File name to encrypt/decrypt
```

Security
--------

1. The crypted message is very easy to crack if the length of key is less than the length of message.
2. In any case, the key is not nescessarily random, which makes this tool as good as a toy.
3. Thus, do not encrypt any real private stuff, it won't protect you from the NSA. *It is just a hack*.

Copying
-------

This project is licensed under the terms of MIT LICENSE, please see LICENSE file for more details.
