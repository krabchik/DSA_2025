def count_tests(test_function, print_every_k: int = 1000):
    count = 0
    while True:
        test_function()
        count += 1
        if not count % print_every_k:
            print(f'Passed {count} tests')
