# Move even elements of array to the beginning (in-place)

import random

from utils import count_tests


def move_even(array: list[int]) -> None:
    even = 0
    current = 0
    array_len = len(array)

    while current < array_len:
        if not array[even] % 2:
            even += 1
        elif not array[current] % 2: # current is even
            array[even], array[current] = array[current], array[even]
            even += 1
        current += 1


def move_even_simple(array: list[int]) -> tuple[list[int], int]:
    even_array = []
    odd_array = []
    for e in array:
        if e % 2:
            odd_array.append(e)
        else:
            even_array.append(e)
    return even_array + odd_array, len(even_array)


def test():
    max_size = 1000 # Max size of array
    size = random.randint(0, max_size)
    max_number = 10000

    array = random.choices(range(max_number), k=size)

    moved_array_true, even_count = move_even_simple(array) # Makes new array

    move_even(array) # Sorts array in-place

    # Check that even parts are equal and odd parts are the same except for order
    assert moved_array_true[:even_count] == array[:even_count]
    assert sorted(moved_array_true[even_count:]) == sorted(array[even_count:])


if __name__ == '__main__':
    count_tests(test)
