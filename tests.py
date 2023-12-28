import unittest
from main import *


class TestRK2(unittest.TestCase):
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
        Dir(1, 'Английский'),
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

    def test_A1(self):
        one_to_many = [(file.filename, file.size, dir.name)
                       for dir in dirs
                       for file in files
                       if file.dir == dir.id]
        self.assertEqual(task1(one_to_many),
                         [('Тест.txt', "Английский"), ("Типовик.pdf", "Право")])

    def test_A2(self):
        one_to_many = [(file.filename, file.size, dir.name)
                       for dir in dirs
                       for file in files
                       if file.dir == dir.id]
        self.assertEqual(task2(one_to_many),
                         [('Английский', 40), ('Право', 67), ('Электротехника', 103)])

    def test_A3(self):
        many_to_many_temp = [(dir.name, fd.dir_id, fd.file_id)
                             for dir in dirs
                             for fd in file_dirs
                             if dir.id == fd.dir_id]

        many_to_many = [(file.filename, file.size, dir_name)
                        for dir_name, dir_id, file_id in many_to_many_temp
                        for file in files
                        if file.id == file_id]

        self.assertEqual(task3(many_to_many),
                         [('Лаб.docx', 103, 'Электротехника'),
                          ('Лаб.docx', 103, '1 модуль'), ('Рис1.png', 524, 'Электротехника'), ('Рис1.png', 524, '1 модуль'),
                          ('Рис2.png', 67, 'Право'), ('Тест.txt', 40, 'Английский'), ('Тест.txt', 40, '2 модуль'),
                          ('фывкапр.pdf', 600, 'Право')])

if __name__ == '__main__':
    unittest.main()
