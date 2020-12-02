# Структура данных «Товары». Представляет список кортежей, хранящих информацию об отдельном товаре.

# В кортеже два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).

product_template = {
    'name': 'Enter a name of product:',
    'price': 'Enter a price of product',
    'amount': 'Enter amount of products',
    'pieces': 'Enter a unit of measure'
}


products_amount = int(input('How many products would you like to add?\n'))

i = 1
product = {}
product_list = []
analytics = {
    'name': [],
    'price': [],
    'amount': [],
    'pieces': []
}

while i <= products_amount:

    # filling product using product template
    for key, ask in product_template.items():
        product[key] = input(ask + '\n')
    product_list.append((i, product))

    # Analytics - a dictionary with product specification as key and list of product specification value as dict value.
    # filling analytics from product dictionary.
    for p in product.keys():
        analytics[p].append(product[p])
    product = {}
    i += 1

print(f'{product_list}\n{analytics}')
