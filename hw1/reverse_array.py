# Reverse array in-place

import random

from utils import count_tests


def reverse_array(array: list[int]) -> None:
    i = 0
    j = len(array) - 1
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1


def test():
    max_size = 1000 # Size of array
    size = random.randint(0, max_size)
    max_number = 10000 # Max element of array
    array = random.choices(range(max_number), k=size)

    reversed_array_true = list(reversed(array)) # Makes new array

    reverse_array(array) # Reverses array in-place

    assert reversed_array_true == array


if __name__ == '__main__':
    count_tests(test)
