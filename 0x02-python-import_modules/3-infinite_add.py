#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    for i in range(len(argv)):
        sum += int(argv[i]) if i > 0 else 0
    print(sum)
