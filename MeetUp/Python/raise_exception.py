#!/usr/bin/python
# This software shows an example to raise an exception.

def raise_an_exception():
    try:
        raise NameError('Oops')
    except NameError as e:
        print(e)

raise_an_exception()
