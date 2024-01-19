#!/usr/bin/python3
for ascii in range(97, 123):
    print("{}".format("" if chr(ascii) in "qe" else chr(ascii)), end='')
