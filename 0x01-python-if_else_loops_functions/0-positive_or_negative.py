#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
	print(number, "is positive")
elif number == 0:
	print(f"{number:d} is zero") #you can print this way
else:
	print("{:d} is negative".format(number)) #you can print this way too
