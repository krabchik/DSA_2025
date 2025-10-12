# Sort array which consists of only 0 and 1

import random

from utils import count_tests


def sort_01(array: list[int]) -> None:
    one = 0

    for current in range(len(array)):
        if not array[current]:
            array[one], array[current] = array[current], array[one]
            one += 1


def test():
    max_size = 1000 # Max size of array
    size = random.randint(0, max_size)
    array = random.choices((0, 1), k=size)

    sorted_array_true = sorted(array) # Makes new array

    sort_01(array) # Sorts array in-place

    assert sorted_array_true == array


if __name__ == '__main__':
    count_tests(test)
