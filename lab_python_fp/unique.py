from gen_random import gen_random


class Unique(object):
    def __init__(self, items, **kwargs):
        self.res = []
        for key, value in kwargs.items():
             if key == 'ignore_case' and value is True:
                items = [i.lower() for i in items]
        for item in items:
            if item not in self.res:
                self.res.append(item)
        pass

    def __next__(self):
        try:
            x = self.res[self.begin]
            self.begin += 1
            return x
        except:
            raise StopIteration

    def __iter__(self):
        self.begin = 0
        return self


def task3():
    print('Проверка работы со списком')
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for item in Unique(data):
        print(item)
    print('Проверка работы с gen_random')
    data = gen_random(10, 1, 3)
    for item in Unique(data):
        print(item)
    print('Проверка ignore_case')
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print('ignore_case False')
    for item in Unique(data):
        print(item)
    print('ignore_case True')
    for item in Unique(data, ignore_case=True):
        print(item)


if __name__ == '__main__':
    task3()
