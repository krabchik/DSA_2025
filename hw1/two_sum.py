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
            return array[i], array[j]
    return None # If such two numbers doesn't exist


def test():
    size = 1000
    max_number = 10000
    array = random.sample(range(1, max_number), size)
    array.sort()

    index_1 = random.randint(0, size - 1)
    index_2 = random.randint(0, size - 1)
    while index_2 == index_1:
        index_2 = random.randint(0, size - 1)
    target = array[index_1] + array[index_2]

    numbers = find_two_sum(array, target)

    assert numbers # Numbers with target sum should exist

    assert target == sum(numbers)


if __name__ == '__main__':
    while True:
        test()