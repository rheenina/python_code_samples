"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для
каждого типа оргтехники.

Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
например словарь.

Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
"""


class WareHouse:
    __current_supplies = []
    __supply_to_ship = []

    def __init__(self, name, amount: int, price: float):
        # Adding first supply to __current_supplies
        self.supply = {"Name": name, "Price": price, "Amount": amount}
        self.__current_supplies.append(self.supply)

    def add_supply(self):
        # Method allows to add products to __current_supplies through input as many as needed.
        while True:
            try:
                name = input('Enter a name and a model of product: ')

                # Quitting the loop if gets q in input.
                if name == 'Q' or name == 'q':
                    break

                amount = int(input('Enter an amount of product: '))
                price = float(input('Enter a price of a product: '))
                supply = {"Name": name, "Price": price, "Amount": amount}

                # Updating __current_supplies with new info about new product.
                self.__current_supplies.append(supply)
                print(f'Current supplies: {self.__current_supplies}\nPress "q" to quit or continue to add supplies.')

            except ValueError:
                print('Only numbers must be used for amount and price.')
                return self.add_supply()

        return self.__current_supplies

    def shipping(self):
        # Method allows to add products to __supply_to_ship through input as many as needed.
        while True:
            try:
                name = input('Enter a name and a model of product: ')

                # Quitting the loop if gets q in input.
                if name == 'Q' or name == 'q':
                    break

                amount = int(input('Enter an amount of product: '))
                price = float(input('Enter a price of a product: '))
                department = input('Where do you want to ship the product? ')
                supply = {"Name": name, "Price": price, "Amount": amount, "Ship to": department}

                # Updating __current_supplies with new info about new product.
                self.__supply_to_ship.append(supply)

            except ValueError:
                print('Only numbers must be used for amount and price.')
                return self.shipping()


class OfficeEquipment:

    def __init__(self, name: str, price: float, amount: int):
        self.name = name
        self.price = price
        self.amount = amount


class Printer(OfficeEquipment):

    def __init__(self, name: str, price: float, amount: int, printer_type):
        super().__init__(name, price, amount)
        self.printer_type = printer_type


class Scanner(OfficeEquipment):

    def __init__(self, name: str, price: float, amount: int, scanner_size):
        super().__init__(name, price, amount)
        self.scanner_size = scanner_size


class Xerox(OfficeEquipment):

    def __init__(self, name: str, price: float, amount: int, xerox_type):
        super().__init__(name, price, amount)
        self.xerox_type = xerox_type
