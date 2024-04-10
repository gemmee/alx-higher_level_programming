#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

try:
    my_rectangle.width = -9
except ValueError as e:
    print(e)
try:
    my_rectangle.height = -9
except ValueError as e:
    print(e)
try:
    my_rectangle.width = "twelve"
except TypeError as e:
    print(e)
try:
    my_rectangle.height = -90.4
except TypeError as e:
    print(e)
