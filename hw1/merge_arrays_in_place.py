# Merge two sorted arrays in-place (first array has extra space)

import random

from utils import count_tests


def merge_two_sorted_arrays_in_place(array1: list[int], len1: int, array2: list[int], len2: int) -> None:
    i = len1 - 1
    j = len2 - 1

    while i >= 0 and j >= 0:
        if array1[i] >= array2[j]:
            array1[i + j + 1] = array1[i]
            i -= 1
        else:
            array1[i + j + 1] = array2[j]
            j -= 1

    while j >= 0:
        array1[j] = array2[j]
        j -= 1


def merge_simple(array1: list[int], array2: list[int]) -> list[int]:
    return sorted(array1 + array2)


def test():
    size = 1000 # Max size of array
    size1, size2 = random.sample(range(size + 1), 2)
    max_number = 10000 # Max element of array
    array1 = sorted(random.choices(range(max_number), k=size1))
    array2 = sorted(random.choices(range(max_number), k=size2))

    merged_array_true = merge_simple(array1, array2) # Makes new array

    array1_with_extra_space = array1 + [0] * size2
    merge_two_sorted_arrays_in_place(array1_with_extra_space, size1, array2, size2) # Merges in first array

    assert array1_with_extra_space == merged_array_true


if __name__ == '__main__':
    count_tests(test)
