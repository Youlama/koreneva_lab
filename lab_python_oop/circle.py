from lab_python_oop.figure import Figure
from lab_python_oop.color import Color
import math


class Circle(Figure):

    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self,  radius, color):
        self.radius = radius
        self.color = Color()
        self.color.color_property = color

    def square(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            Circle.get_figure_type(), self.color.color_property, self.radius, self.square())
