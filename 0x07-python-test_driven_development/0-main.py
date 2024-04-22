#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print("#" * 33)
print(add_integer(None))
print(add_integer(100.3, -2))
