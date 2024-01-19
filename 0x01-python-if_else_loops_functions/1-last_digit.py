#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10 if number >= 0 else number % -10
s = f"Last digit of {number:d} is {ld:d}"
if ld > 5:
    print(f"{s} and is greater than 5")
elif ld == 0:
    print(f"{s} and is 0")
else:
    print(f"{s} and is less than 6 and not 0")
