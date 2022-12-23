#!/bin/usr/python3

def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.
    
    sentence: the string
    """
    s_len = len(sentence)
    if (s_len == 0):
        f_char = None
    else:
        f_char = sentence[0]
    return ((s_len, f_char))
