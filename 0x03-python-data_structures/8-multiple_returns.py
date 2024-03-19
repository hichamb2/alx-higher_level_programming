#!/usr/bin/python3

def multiple_returns(sentence):
    len_str = len(sentence)
    if sentence:
        char = sentence[0]
    else:
        char = None
    tuple_str = (len_str, char)
    return (tuple_str)
