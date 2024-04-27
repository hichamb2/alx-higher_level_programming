#!/usr/bin/python3
"""define a function"""

def say_my_name(first_name, last_name):
    """function/method that print name"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(first_name, last_name)
