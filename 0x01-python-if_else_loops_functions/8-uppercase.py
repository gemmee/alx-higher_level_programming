#!/usr/bin/python3
def uppercase(str):
    for i in str:
        i = chr(ord(i) - 32) if ord('a') <= ord(i) <= ord('z') else i
        print("{}".format(i), end='')
    print("{}".format("\n"), end='')  # prints new line with string format
