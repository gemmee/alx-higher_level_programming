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
    text = text.strip()
    letters = []
    flag = 0
    for letter in text:
        if letter in ".?:":
            flag = 1
            letters.append(f"{letter}\n\n")
        else:
            if not flag:
                letters.append(letter)
            else:
                if letter != " ":
                    letters.append(letter)
                    flag = 0
    print("".join(letters), end="")
