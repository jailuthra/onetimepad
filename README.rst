One-Time-Pad Python
===================

**One-Time-Pad Python is a command-line encryption tool**, which uses an
encryption mechanism very similar to `One-time Pad`_ (Duh. Thanks for
telling that)

Features
--------

-  It can be used as a python script, or can be imported as a module.
-  You can encrypt/decrypt data not only from stdin, but from a file
   too.
-  It is Open Source! :D

Security
--------

1. The crypted message is very easy to crack if the length of key is
   less than the length of message.
2. In any case, the key is not nescessarily random, which makes this
   tool as good as a toy.
3. Thus, do not encrypt any real private stuff, it won’t protect you
   from the NSA. *It is just a hack*.

Copying
-------

This project is licensed under the terms of MIT LICENSE, please see
LICENSE file for more details.

.. _One-time Pad: https://en.wikipedia.org/wiki/One-time_pad
