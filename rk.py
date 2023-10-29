# используется для сортировки
from operator import itemgetter

class File:
    """Файл"""

    def __init__(self, id, filename, size, dir_id):
        self.id = id
        self.filename = filename
        self.size = size
        self.dir = dir_id

class Dir:
    """Каталог файлов"""

    def __init__(self, id, name):
        self.id = id
        self.name = name

class FileDir:
    """
    'Файлы каталога файлов' для реализации
    связи многие-ко-многим
    """

    def __init__(self, dir_id, file_id):
        self.dir_id = dir_id
        self.file_id = file_id

# Файлы
files = [
    File(1, 'Тест.txt', 40, 1),
    File(2, 'Лаб.docx', 103, 2),
    File(3, 'Рис1.png', 524, 2),
    File(4, 'Рис2.png', 67, 3),
    File(5, 'Типовик.pdf', 600, 3),
]

# Каталоги
dirs = [
    Dir(1, 'Английскийй'),
    Dir(2, 'Электротехника'),
    Dir(3, 'Право'),
    Dir(4, '1 модуль'),
    Dir(5, '2 модуль'),
]

file_dirs = [
    FileDir(1, 1),
    FileDir(2, 2),
    FileDir(2, 3),
    FileDir(3, 4),
    FileDir(3, 5),
    FileDir(4, 2),
    FileDir(4, 3),
    FileDir(5, 1),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(file.filename, file.size, dir.name)
                   for dir in dirs
                   for file in files
                   if file.dir == dir.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(dir.name, fd.dir_id, fd.file_id)
                         for dir in dirs
                         for fd in file_dirs
                         if dir.id == fd.dir_id]

    many_to_many = [(file.filename, file.size, dir_name)
                    for dir_name, dir_id, file_id in many_to_many_temp
                    for file in files
                    if file.id == file_id]

    print('Задание 1')
    res1 = []
    for i in one_to_many:
        if i[0].startswith('Т'):
            res1.append((i[0], i[2]))
    print(res1)
    print('\nЗадание 2')
    res2 = []
    for dir in dirs:
        df = list(filter(lambda i: i[2] == dir.name, one_to_many))
        if len(df) > 0:
            sizes = [size for _, size, _ in df]
            min_size = min(sizes)
            res2.append((dir.name, min_size))
    print(sorted(res2, key=itemgetter(1)))

    print('\nЗадание 3')
    res3 = sorted(many_to_many, key=itemgetter(0))
    print(res3)

if __name__ == '__main__':
    main()
