#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    '''
    Deletes keys with a specific value in a dictionary.

    a_dictionary: the dictionary
    value: the value for which all keys should be deleted

    Description:
        - If the value doesn’t exist, the dictionary won’t change
        - All keys having the searched value have to be deleted
        - You are not allowed to import any module

    '''
    key = []
    for k, v in a_dictionary.items():
        if v == value:
            key.append(k)
    for i in key:
        del a_dictionary[i]
    return (a_dictionary)
