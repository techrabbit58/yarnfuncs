"""Test the roman to decimal library."""
import pytest

from roman_numbers import *

test_cases = [
    ('I', 1),
    ('II', 2),
    ('IV', 4),
    ('IVI', None),
    ('V', 5),
    ('VIII', 8),
    ('VIIII', None),
    ('IX', 9),
    ('IXI', None),
    ('X', 10),
    ('XXX', 30),
    ('XL', 40),
    ('L', 50),
    ('XC', 90),
    ('XXXXC', None),
    ('C', 100),
    ('CCCXXXIII', 333),
    ('CD', 400),
    ('CDCD', None),
    ('D', 500),
    ('DD', None),
    ('DCM', None),
    ('DCCLIII', 753),
    ('CM', 900),
    ('M', 1000),
    ('MCMLVIII', 1958),
    ('MCMLIX', 1959),
    ('MCMLXXXIX', 1989),
    ('MMVI', 2006),
    ('MMXVIII', 2018),
    ('MMXIX', 2019),
    ('MMXXI', 2021),
    ('MMMCMXCIX', 3999),
    ('MMMMCMXCIX', None),
    ('ICDMV', None),
    ('MMMMM', None),
    ('ABC', None),
    ('MCMXLIX', 1949),
    ('MCDXCII', 1492),
    ('XLII', 42),
    ('MDCLXVI', 1666),
    (None, 5000),
    (None, 12345),
    (None, 0),
    (None, -8765283),
    ('MDCCXCVIII', 1798),
    ('MCMXCVII', 1997),
]


@pytest.mark.parametrize('roman_number, decimal_number', [tc for tc in test_cases if not tc[0] is None])
def test_roman_to_decimal(roman_number, decimal_number):
    assert roman_to_decimal(roman_number) == decimal_number


@pytest.mark.parametrize('roman_number, decimal_number', [tc for tc in test_cases if not tc[1] is None])
def test_decimal_to_roman(roman_number, decimal_number):
    assert decimal_to_roman(decimal_number) == roman_number


# last line of code
