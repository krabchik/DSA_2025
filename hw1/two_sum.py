import random


def find_two_sum(array: list[int], target: int) -> tuple[int, int] | None:
    i = 0
    j = len(array) - 1
    while i < j:
        two_sum = array[i] + array[j]
        if two_sum < target:
            i += 1
        elif two_sum > target:
            j -= 1
        else:
            return i, j
    return None # If such two numbers doesn't exist


def test():
    size = 1000 # Size of array
    max_number = 10000 # Max element of array
    array = random.sample(range(1, max_number), size)
    array.sort()

    index_1 = random.randint(0, size - 1)
    index_2 = random.randint(0, size - 1)
    while index_2 == index_1:
        index_2 = random.randint(0, size - 1)
    target = array[index_1] + array[index_2]

    indexes = find_two_sum(array, target)

    assert indexes # Numbers with target sum should exist

    assert target == array[indexes[0]] + array[indexes[1]]


if __name__ == '__main__':
    while True:
        test()