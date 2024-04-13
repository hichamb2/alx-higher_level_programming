#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value and isinstance(value, int):
            print("{:d}".format(value))
            return (True)
    except TypeError:
        return (False)
