#!/usr/bin/python3
def element_at(my_list, idx):
    if idx >= len(my_list) or idx < 0:
        return (None)
    num = my_list[idx]
    del my_list[idx]
    return (num)
