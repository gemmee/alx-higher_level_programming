#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{}.format(chr(ord(i))), end="")
    print()
