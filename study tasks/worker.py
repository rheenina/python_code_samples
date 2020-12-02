"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход).

Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия.

Класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника, дохода с учетом премии.
"""


class Worker:

    def __init__(self, name, surname, position, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage: float, bonus: float):
        super().__init__(name, surname, position, wage, bonus)

    # получение полного имени сотрудника
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    # доход с учетом премии
    def get_total_income(self):
        total_income = float(self._income['wage']) + float(self._income['bonus'])
        return total_income
