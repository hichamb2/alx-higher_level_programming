#!/usr/bin/python3
element_at = __import__('1-element_at').element_at
print_list_integer = __import__('0-print_list_integer').print_list_integer
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
print_list_integer(my_list)
