from random import randint


def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield randint(begin, end)


def task2():
    print(*gen_random(5, 1, 3), sep=', ')


if __name__ == '__main__':
    task2()
