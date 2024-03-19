#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    max_n = my_list[0]
    for i in range(0, len(my_list)):
        if max_n < my_list[i]:
            max_n = my_list[i]
        else:
            max_n = max_n
    return (max_n)
