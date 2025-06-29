from functools import reduce


def sum_of_digits(number):
    return reduce(lambda digit1, digit2: int(digit1) + int(digit2), str(number))