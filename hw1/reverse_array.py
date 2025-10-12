# Reverse array in-place

import random
from copy import deepcopy


def reverse_array(array: list[int]) -> None:
    i = 0
    j = len(array) - 1
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1


def test():
    size = 1000 # Size of array
    max_number = 10000 # Max element of array
    array = random.sample(range(1, max_number), size)

    new_array = deepcopy(array)
    reverse_array(new_array) # Reverses array in-place

    assert list(reversed(array)) == new_array


if __name__ == '__main__':
    while True:
        test()
