import math

# The right shift operation is similar to floor division by powers of two.
# Write a function that mimics the right shift operator and returns the result from the two given integers.
def shift_to_right(x, y):
    if y < 0:
        raise ValueError("Sorry, no numbers below zero")

    return math.floor(x / 2 ** y)

# Create a function that takes a number num and returns its length.
def number_length(num):
    length = 0
    for _ in str(num):
        length += 1
    return length