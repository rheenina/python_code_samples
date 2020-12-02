"""
Скрипт расчета заработной платы сотрудника. В расчете использована формула: (выработка в часах*ставка в
час) + премия. Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

# 1st trash variable for file name, last trash variable for anything that would be written after bonus
_, hours, hour_pay, bonus, *_ = argv


def salary(hours: float, hour_pay: float, bonus: float):
    # Calculating month salary with bonus
    month_salary = hours * hour_pay + bonus
    return month_salary


try:
    employee_salary = salary(float(hours), float(hour_pay), float(bonus))
    print(f"Salary is {employee_salary}.")
except ValueError:
    print("Enter only numbers to calculate a salary!")
