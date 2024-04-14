#!/usr/bin/python3
"""defines a square"""


class Square:
    """defines a square"""
    def __init__(self, size):
        if not isinstance(size, int):
            print('size must be an integer')
        elif size < 0:
            ('size must be >= 0')
        self.__size = size
