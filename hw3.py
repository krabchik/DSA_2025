import random


def integer_root(target: int):
    l = 0
    r = target
    while l <= r:
        m = l + (r - l) // 2
        if m * m > target:
            r = m - 1
        elif m * m < target:
            l = m + 1
        else:
            return m
    return r

def feed_animals(animals: list[int], food: list[int]):
    animals_n = len(animals)
    animals = sorted(animals)
    food = sorted(food)
    animal_i = 0
    for f in food:
        if f >= animals[animal_i]:
            animal_i += 1
        if animal_i == animals_n:
            break
    return animal_i

def find_extra_letter(original: str, new: str):
    count = dict()
    for letter in original:
        count[letter] = count.get(letter, 0) + 1
    for letter in new:
        if count.get(letter, 0) == 0:
            return letter
        count[letter] -= 1
    return ''

def find_two_sum_in_arbitrary_array(array: list[int], target: int):
    values = dict()
    for i in range(len(array)):
        diff = target - array[i]
        if diff in values:
            return values[diff], i
        values[array[i]] = i
    return ()

def shell_sort(array: list[int]):
    n = len(array)
    d = len(array) // 2
    while d > 0:
        for curr in range(d, n):
            prev = curr - d
            while prev >= 0 and array[prev] > array[curr]:
                array[curr], array[curr - d] = array[curr - d], array[curr]
                curr = prev
                prev -= d
            curr += 1
        d //= 2

def group_anagrams(words: list[str]):
    words_stats = []
    groups = []
    for word in words:
        word_stat = dict()
        for letter in word:
            word_stat[letter] = word_stat.get(letter, 0) + 1
        if word_stat in words_stats:
            groups[words_stats.index(word_stat)].append(word)
        else:
            words_stats.append(word_stat)
            groups.append([word])
    return groups

def test_integer_root():
    for target in random.sample(range(10_000_000), 1000):
        assert integer_root(target) == int(target ** 0.5)

def test_feed_animals():
    assert feed_animals([3, 2, 1], [1, 0, 1]) == 1
    assert feed_animals([3, 2, 1], [2, 1, 1]) == 2
    assert feed_animals([3, 2, 1], [7, 5, 3, 1]) == 3

def test_find_extra_letter():
    assert find_extra_letter('abc', 'acbc') == 'c'
    assert find_extra_letter('abc', 'abca') == 'a'
    assert find_extra_letter('abc', 'eabc') == 'e'
    assert find_extra_letter('abc', 'abce') == 'e'
    assert find_extra_letter('abc', 'abc') == ''

def test_find_two_sum_in_arbitrary_array():
    assert find_two_sum_in_arbitrary_array([3, 1, 7, 0], 1)  == (1, 3)
    assert find_two_sum_in_arbitrary_array([3, 1, 7, 0], 10) == (0, 2)
    assert find_two_sum_in_arbitrary_array([3, 1, 7, 1], 2)  == (1, 3)
    assert find_two_sum_in_arbitrary_array([3, 1, 7, 0], 0)  == ()

def test_shell_sort():
    for _ in range(1000):
        array = list(range(1000))
        random.shuffle(array)
        sorted_array = sorted(array)
        shell_sort(array)
        assert array == sorted_array

def test_group_anagrams():
    assert group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert group_anagrams(['won', 'now', 'aaa', 'ooo', 'ooo']) == [['won', 'now'], ['aaa'], ['ooo', 'ooo']]

def test_all():
    test_integer_root()
    test_feed_animals()
    test_find_extra_letter()
    test_find_two_sum_in_arbitrary_array()
    test_shell_sort()
    test_group_anagrams()

if __name__ == '__main__':
    test_all()
