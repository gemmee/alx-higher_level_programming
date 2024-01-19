#!/usr/bin/python3
for ascii in range(97, 123):
    print("{}".format("" if chr(ascii) in "qe" else chr(ascii)), end='')
'''
for i in range(ord('a'), ord('z') + 1):
    if (i != ord('q') and i != ord('e')):
        print("{}".format(chr(i)), end="")
'''
