#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element 2 lists.

    my_list_1: the first list that can contain any type
    my_list_2: the second list that can contain any type
    list_length: can be bigger than the length of both lists

    Return: a new list with all divisions
    Description:
        - If 2 elements can't be divided, the division result would be 0
        - If an element is not an integer or float, print: wrong type
        - If division can't be done, print: division by 0
        - If my_list_1 or my_list_2 is too short, print: out of range
        - You have to use try: /except: /finally:
        - You are not allowed to import any module
    """
    result = []
    for i in range(list_length):
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            result.append(div)
    return (result)
