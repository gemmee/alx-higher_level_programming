#!/usr/bin/python3

def weight_average(my_list=[]):
    '''
    Returns the weighted average of all integers tuple (<score>, <weight>)

    my_list: the list

    Description: You are not allowed to import any module( such as functools)
    '''
    if my_list == [] or type(my_list) is not list:
        return (0)
    sum = 0
    total = 0
    for score, weight in dict(my_list).items():
        sum += score * weight
        total += weight
    average = sum / total
    return (average)
