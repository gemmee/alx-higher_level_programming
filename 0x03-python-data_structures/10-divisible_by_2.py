#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]  # make copy of my_list
    for i in range(len(new_list)):
        new_list[i] = False if new_list[i] % 2 else True
    return new_list
