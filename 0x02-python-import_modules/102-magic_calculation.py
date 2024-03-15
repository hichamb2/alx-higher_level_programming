#!/usr/bin/python3
def magic_calculation(x, y):
    from magic_calculation_102 import add, sub

    if x < y:
        a = add(x, y)
        for i in range(4, 6):
            a = add(a, i)
        return (a)
    else:
        return (sub(x, y))
