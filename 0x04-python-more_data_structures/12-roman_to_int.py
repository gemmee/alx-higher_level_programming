#!/usr/bin/python3

def roman_to_int(roman_string):
    '''
    Converts a Roman numeral into its equivalent integer.

    roman_string: the roman numeral

    Description:
        - You can assume the number will be between 1 to 3999.
        - If the roman_string is not a string or None, return 0
    '''
    if roman_string is None or type(roman_string) is not str:
        return (0)
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    roman_string = roman_string.upper()
    result = 0
    for i in range(len(roman_string)):
        if i > 0 and roman[roman_string[i]] > roman[roman_string[i-1]]:
            result += roman[roman_string[i]] - roman[roman_string[i-1]] * 2
        else:
            result += roman[roman_string[i]]
    return (result)
