# -*- coding: utf-8 -*-
__author__ = 'florije'

"""
这里也可以写
"""
# python -m doctest unnecessary_math.py
# python -m doctest -v unnecessary_math.py

def multiply(a, b):
    """
    >>> multiply(2,3)
    6
    >>> multiply('baka~',3)
    'baka~baka~baka~'
    """
    return a * b


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
