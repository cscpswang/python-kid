# _*_coding=utf-8_*_
# __author__='xj'
"""doc test example"""

def abs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    -1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)

import doctest
doctest.testmod()