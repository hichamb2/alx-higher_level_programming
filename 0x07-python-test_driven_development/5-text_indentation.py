#!/usr/bin/python3
"""define a function"""


def text_indentation(text):
    """function/method that add 2 integers"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while (i < len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("{}".format(text[i]))
            print("\n", end="")
            while (i < len(text) and text[i + 1] == ' '):
                i = i + 1
        else:
            print("{}".format(text[i]), end="")
        i += 1
