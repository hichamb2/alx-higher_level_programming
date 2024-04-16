#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 3)
print(my_rectangle.width)
print(my_rectangle.height)
try:
    my_rectangle = Rectangle("2", 3)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
try:
    my_rectangle = Rectangle(2, "3")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    my_rectangle = Rectangle(2, 3)
    my_rectangle.width = -4
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
try:
    my_rectangle = Rectangle(2, 3)
    my_rectangle.width = "4"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
