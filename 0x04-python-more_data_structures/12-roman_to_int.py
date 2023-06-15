#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0
    digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    total = 0
    for roman in reversed(roman_string):
        arabic = digits[roman]
        total += arabic if total < arabic * 5 else -arabic
    return total
