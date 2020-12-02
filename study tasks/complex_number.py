"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел.
"""


class ComplexNum:

    def __init__(self, a, b):
        self.a_number = a
        self.b_number = b

    def __str__(self):
        return f'{self.a_number} + {self.b_number}j'

    def __add__(self, other):
        a = (self.a_number + other.a_number)
        b = (self.b_number + other.b_number)
        return ComplexNum(a, b)

    def __mul__(self, other):
        a = (self.a_number * other.a_number) - (self.b_number * other.b_number)
        b = (self.b_number * other.a_number) + (self.a_number * other.b_number)
        return ComplexNum(a, b)
