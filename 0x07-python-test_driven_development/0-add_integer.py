#!/usr/bin/python3
"""define a function"""


def add_integer(a, b):
    """function/method that add 2 integers"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
