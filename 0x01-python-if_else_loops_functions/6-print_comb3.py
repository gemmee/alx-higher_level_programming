#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i+1, 10):
        print(f'{i}{j}' + "{}".format("\n" if i + j == 17 else ", "), end='')
