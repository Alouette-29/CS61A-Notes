"""
In terminal:
python -m doctest higher_order.py
More verbose:
python -m doctest -v higher_order.py
"""

from math import sqrt


def sum_naturals(n):
    """
    >>> sum_naturals(5)
    15
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total


def search(f):
    """
    @param f: f is a function
    @return: the first positive number s.t. f(x) is True
    >>> is_three = lambda x: x == 3
    >>> search(is_three)
    3
    """
    x = 0
    # while True:
    #     if f(x):
    #         return x
    #     x += 1
    while not f(x):
        x += 1
    return x


def inverse(f):
    """
    @param f: f is a function
    @return: g, the inverse of f, s.t. g(f(x)) = g(y) = x

    the param passed to `search` is a fuction deciding if f(x) == y is true or not
    the value `search` returns is the x, satisfying f(x) == y
    the return function `g` satisfies, given y = f(x) (we have just search for this y), it always output x
    this lambda function takes y as an input, and always output x, satisfying f(x) == y
    so it's the inverse of f

    >>> square = lambda x: x * x
    >>> sqrt = inverse(square)
    >>> sqrt(4)
    2
    """
    return lambda y: search(lambda x: f(x) == y)


def real_sqrt(x):
    """
    >>> real_sqrt(4)
    2.0
    >>> real_sqrt(-1)
    0.0
    """
    return sqrt(x) if x > 0 else 0.0
