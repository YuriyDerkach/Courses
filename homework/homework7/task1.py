import random

# Задание №1
# У вас есть словарь, где ключ – название продукта. Значение –
# список, который содержит цену и кол-во товара.
# Выведите через ‘’–’’ название – цену – количество.
# С клавиатуры вводите название товара и его кол-во. n – выход
# из программы. Посчитать цену выбранных товаров и сколько
# товаров осталось в изначальном списке.

def prod_out(prod_dict):
    for key, value in prod_dict.items():
        print(key, end='')
        for num in value:
            print(' -', num, end='')
        print()

products_dict = {
    'макароны': [6.15, random.randint(0, 40)],
    'вафли': [0.69, random.randint(0, 40)],
    'лаваш': [1.49, random.randint(0, 40)],
    'молоко': [1.79, random.randint(0, 40)],
    'масло': [3.39, random.randint(0, 40)],
    'сыр': [5.25, random.randint(0, 40)],
    'кофе': [5.99, random.randint(0, 40)],
    'чай': [5.49, random.randint(0, 40)],
}
print(products_dict['вафли':'лаваш'])
taken_dict = {}

prod_out(products_dict)

while True:
    product = input('Товар: ').lower()
    if product == 'выход':
        break
    elif product in products_dict.keys():
        product_count = int(input('Кол-во: '))
        if product_count <= products_dict[product][1]:
            products_dict[product][1] -= product_count
            if product in taken_dict.keys():
                taken_dict[product][0] += products_dict[product][0] * product_count
                taken_dict[product][1] += product_count
            else:
                taken_dict[product] = [products_dict[product][0] * product_count, product_count]
            print('У нас осталось {} {}.'.format(products_dict[product][1], product))
        else:
            print('У нас только {} {}.'.format(products_dict[product][1], product))
    else:
        print('У нас нету такого товара.')

print('Оставшиеся товары:')
prod_out(products_dict)
print('Купленные товары:')
prod_out(taken_dict)
