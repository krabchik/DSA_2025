import random

from utils import count_tests


def move_zeros_to_end(array: list[int]) -> None:
    zero = len(array) - 1
    current = zero
    array_len = len(array)

    while current >= 0:
        if not array[zero]:
            zero -= 1
        elif not array[current]:
            array[zero], array[current] = array[current], array[zero]
            zero -= 1
        current -= 1


def move_zeros_simple(array: list[int]) -> tuple[list[int], int]:
    zero_count = array.count(0)
    non_zero_array = [e for e in array if e]
    return non_zero_array + [0] * zero_count, zero_count


def test():
    max_size = 1000 # Max size of array
    size = random.randint(0, max_size)
    max_number = 10000

    array = random.choices(range(max_number), k=size)

    moved_array_true, zero_count = move_zeros_simple(array) # Makes new array

    move_zeros_to_end(array) # Sorts array in-place

    # Check that zeros parts are equal and odd parts are the same except for order
    assert moved_array_true[-zero_count:] == array[-zero_count:]
    assert sorted(moved_array_true[:-zero_count]) == sorted(array[:-zero_count])


if __name__ == '__main__':
    count_tests(test)
