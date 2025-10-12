import random

from utils import count_tests


def sort_012(array: list[int]) -> None:
    left = 0
    current = 0
    right = len(array) - 1

    while current <= right:
        current_val = array[current]
        if current_val == 0 and current != left:
            array[left], array[current] = current_val, array[left]
            left += 1
        elif current_val == 2 and current != right:
            array[current], array[right] = array[right], current_val
            right -= 1
        else:
            current += 1


def test():
    max_size = 1000 # Max size of array
    size = random.randint(0, max_size)

    array = random.choices((0, 1, 2), k=size)

    sorted_array_true = sorted(array) # Makes new array

    sort_012(array) # Sorts array in-place

    assert sorted_array_true == array


if __name__ == '__main__':
    count_tests(test)
