def field(items, *args):
    assert len(args) > 0
    res = []
    for item in items:
        tmp = {}
        for arg in args:
            if item[arg] is not None:
                tmp[arg] = item[arg]
        if tmp:
            res.append(tmp)
    return tuple(res)


def task1():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    print(*[el for el in field(goods, 'title')], sep=', ')
    print(*field(goods, 'title', 'price'), sep=', ')


if __name__ == '__main__':
    task1()
