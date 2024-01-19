#!/usr/bin/python3
for i in range(0, 100):
    print(f"{i:02}" + "{}".format("\n" if i == 99 else ", "), end="")
