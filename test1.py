import unittest
from modify_levenstain import levenstain

class LevenstainTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(levenstain("", "пустыня"), 7)
    def test_equal(self):
        self.assertEqual(levenstain("пустыня", "пустыня"), 0)
    def test_differ (self):
        self.assertEqual(levenstain("ложка","лодка"), 1)

if __name__ == '__main__':
    unittest.main()