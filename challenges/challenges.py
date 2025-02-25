import math


def shift_to_right(x, y):
    if y < 0:
        raise ValueError("Sorry, no numbers below zero")

    return math.floor(x / 2 ** y)