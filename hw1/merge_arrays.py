# Merge two sorted arrays into a new array

import random

from utils import count_tests


def merge_two_sorted_arrays(array1: list[int], array2: list[int]) -> list[int]:
    i, j = 0, 0
    len1, len2 = len(array1), len(array2)
    resulting_array: list[int] = [0] * (len1 + len2)

    while i < len1 and j < len2:
        if array1[i] <= array2[j]:
            resulting_array[i + j] = array1[i]
            i += 1
        elif array1[i] > array2[j]:
            resulting_array[i + j] = array2[j]
            j += 1

    while i < len1:
        resulting_array[i + j] = array1[i]
        i += 1
    while j < len2:
        resulting_array[i + j] = array2[j]
        j += 1

    return resulting_array


def merge_simple(array1: list[int], array2: list[int]) -> list[int]:
    return sorted(array1 + array2)


def test():
    size = 1000 # Max size of array
    size1, size2 = random.sample(range(size + 1), 2)
    max_number = 10000 # Max element of array

    array1 = sorted(random.choices(range(max_number), k=size1))
    array2 = sorted(random.choices(range(max_number), k=size2))

    merged_array = merge_two_sorted_arrays(array1, array2) # Makes new array

    merged_array_true = merge_simple(array1, array2) # Makes new array

    assert merged_array == merged_array_true


if __name__ == '__main__':
    count_tests(test)
