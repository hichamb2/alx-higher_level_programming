#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    A = len(tuple_a)
    B = len(tuple_b)
    if A == 0:
        tuple_a = (0, 0)
    elif A == 1:
        tuple_a = (tuple_a[0], 0)
    if B == 0:
        tuple_b = (0, 0)
    elif B == 1:
        tuple_b = (tuple_b[0], 0)
    new_tuble = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuble
