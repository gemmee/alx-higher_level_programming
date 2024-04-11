#!/usr/bin/python3
'''
This is the "5-text_indentation" module.

It has one function, text_indentation().
A doctest has been written for this module
under the ./tests directory and can be run as:
python3 -m doctest -v ./tests/5-text_indentation.txt
'''


def text_indentation(text):
    '''Prints a text with 2 new lines after each of these characters(. ? :)

    Args:
        text: a string of text
    Returns:
        None
    Raises:
        TypeError: if text is not a string
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    list_of_lines = text.replace(".", ":").replace("?", ":").split(":")
    count_line = 0
    for line in list_of_lines:
        count_line += 1
        ends = '' if count_line == len(list_of_lines) else '\n\n'
        print(line.strip(), end=ends)
