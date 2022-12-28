#!/usr/bin/python3

def search_replace(my_list, search, replace):
    '''
    Replaces all occurrences of an element by another in a new list.

    my_list: the list
    search: the element to be replaced
    replace: the new element
    '''
    new_list = list(my_list)
    for i in range(len(new_list)):
        if search == new_list[i]:
            new_list[i] = replace
    return new_list
