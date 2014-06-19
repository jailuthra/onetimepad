===================
One-Time-Pad Python
===================

**One-Time-Pad Python is a command-line encryption tool**, which uses an
encryption mechanism very similar to `One-time Pad`_ (Duh. Thanks for
telling that)

Installation
------------

Install it using pip::

    $ pip install onetimepad

Usage
-----

To use it from the command-line, run::

    $ onetimepad

Or, import the onetimepad module in your script::

    #!/usr/bin/env python3

    import onetimepad

    cipher = onetimepad.encrypt('some text', 'a_random_key')
    msg = onetimepad.decrypt(cipher, 'a_random_key')

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
