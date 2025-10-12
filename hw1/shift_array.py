# Right rotate array by n elements through reversing array

import random

from utils import count_tests


def reverse_array_part(array: list[int], left: int, right: int) -> None:
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1


def shift_array(array: list[int], n: int) -> None:
    index = n - 1
    size = len(array)
    reverse_array_part(array, 0, size - 1)
    reverse_array_part(array, 0, index)
    reverse_array_part(array, index + 1, size - 1)


def shift_array_simple(array: list[int], n: int) -> list[int]:
    return array[-n:] + array[:-n]


def test():
    size = 1000 # Size of array
    max_number = 10000 # Max element of array
    array = random.choices(range(max_number), k=size)
    n = random.randint(0, size) # Amount to shift

    shifted_array_true = shift_array_simple(array, n) # Makes new array

    shift_array(array, n) # Shifts in-place

    assert shifted_array_true == array


if __name__ == '__main__':
    count_tests(test)
