"""Functions to convert between arabic/decimal number and roman number representation."""

from collections import namedtuple

RomanCodeRule = namedtuple('RomanCodeRule', 'max_repeats value ascendant descendant')

EMPTY_STRING = ''

code_rule = {
    'M': RomanCodeRule(3, 1000, 'CM', 'CM'),
    'CM': RomanCodeRule(1, 900, 'XC', 'D'),
    'D': RomanCodeRule(1, 500, 'C', 'CD'),
    'CD': RomanCodeRule(1, 400, 'XC', 'C'),
    'C': RomanCodeRule(3, 100, 'XC', 'XC'),
    'XC': RomanCodeRule(1, 90, 'IX', 'L'),
    'L': RomanCodeRule(1, 50, 'X', 'XL'),
    'XL': RomanCodeRule(1, 40, 'IX', 'X'),
    'X': RomanCodeRule(3, 10, 'IX', 'IX'),
    'IX': RomanCodeRule(1, 9, None, 'V'),
    'V': RomanCodeRule(1, 5, 'I', 'IV'),
    'IV': RomanCodeRule(1, 4, None, 'I'),
    'I': RomanCodeRule(3, 1, None, None),
}


def roman_to_decimal(roman_number):
    result = 0
    roman_digit = 'M'
    while not roman_digit is None:
        repeats_granted = code_rule[roman_digit].max_repeats
        while repeats_granted > 0:
            if roman_number.startswith(roman_digit):
                result += code_rule[roman_digit].value
                roman_number = roman_number.replace(roman_digit, EMPTY_STRING, 1)
                repeats_granted -= 1
            else:
                roman_digit = code_rule[roman_digit].descendant
                break
        else:
            roman_digit = code_rule[roman_digit].ascendant
    return result if len(roman_number) == 0 else None


def relaxed_roman_to_decimal(roman_number):
    result = 0
    roman_digits = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    while not len(roman_digits) == 0:
        roman_digit = roman_digits[0]
        while roman_number.startswith(roman_digit):
            roman_number = roman_number[len(roman_digit):]
            result += code_rule[roman_digit].value
        roman_digits = roman_digits[1:]
    return result


def decimal_to_roman(decimal_number):
    result = ''
    roman_digit = 'M'
    while not roman_digit is None:
        repeats_granted = code_rule[roman_digit].max_repeats
        roman_digit_value = code_rule[roman_digit].value
        while repeats_granted > 0:
            if decimal_number >= roman_digit_value:
                result += roman_digit
                decimal_number -= roman_digit_value
                repeats_granted -= 1
            else:
                roman_digit = code_rule[roman_digit].descendant
                break
        else:
            roman_digit = code_rule[roman_digit].ascendant
    return result if decimal_number == 0 and result != EMPTY_STRING else None


__all__ = 'roman_to_decimal relaxed_roman_to_decimal decimal_to_roman'.split()

# last line of code
