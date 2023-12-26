from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import numpy as np


def main():
    r = Rectangle(15, 15, "синего")
    print(r.__repr__())
    c = Circle(15, "зеленого")
    print(c.__repr__())
    s = Square(15, "красного")
    print(s.__repr__())
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print(a)


if __name__ == "__main__":
    main()
