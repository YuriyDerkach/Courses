import pprint

# 5. Клиент приходит в кондитерскую. Он хочет приобрести один или несколько видов
# продукции, а также узнать её состав.
# Реализуйте кондитерскую.
# У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и
# т.д.). Значение – список, который содержит состав, цену (за 100гр) и кол-во (в
# граммах).
# Предложите выбор:
# 1. Если человек хочет посмотреть описание: название – описание
# 2. Если человек хочет посмотреть цену: название – цена.
# 3. Если человек хочет посмотреть количество: название – количество.
# 4. Всю информацию.
# 5. Приступить к покупке:
# С клавиатуры вводите название торта и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном
# списке
# 6. До свидания

products = {
            'торт': [
                    ['тесто', 'шоколад', 'взбитые сливки', 'крем'], 3.0, 3000
                    ],
            'печенье': [
                    ['тесто', 'шоколад'], 2.0, 2000
                    ],
            'кекс': [
                    ['тесто', 'шоколад', 'изюм'], 1.0, 1500
                    ],
            'круассан': [
                    ['тесто', 'шоколад'], 1.5, 1000
                    ]
            }

goods = {}

print('Добрый день, что Вы хотите?\n'
      'Введите 1, если хотите получить информацию о товаре.\n'
      'Введите 2, если хотите приступить к покупке.\n'
      'Введите n для выхода.')
while True:
    choice = input()
    if choice == '1':
        print('Выберите товар:')
        for prod in products.keys():
            print(prod)
        while True:
            prod_choice = input()
            try:
                print('Какую информацию о товаре Вы хотите получить?\n'
                      '1 - состав.\n'
                      '2 - цена.\n'
                      '3 - количество.\n'
                      'n - выход.')
                while True:
                    info = input()
                    if info == '1':
                        print('{} - {}.'.format(prod_choice, ', '.join(products[prod_choice.lower()][0])))
                    elif info == '2':
                        print('{} - {}р за 100г.'.format(prod_choice, products[prod_choice.lower()][1]))
                    elif info == '3':
                        print('{} - {}г.'.format(prod_choice, products[prod_choice.lower()][2]))
                    elif info == 'n':
                        break
                    else:
                        print('Вы ввели неверно, попробуйте еще раз.')
                        continue
                    break
            except KeyError:
                print('Вы указали неверный товар, попробуйте снова.')
            break
    elif choice == '2':
        while True:
            print('Выберите товар:')
            for prod in products.keys():
                print(prod)
            print('n - выход.')
            prod_choice = input()
            if prod_choice == 'n':
                break
            try:
                print('Сколько грамм?')
                while True:
                    gramms = int(input())
                    if gramms <= products[prod_choice.lower()][2]:
                        if prod_choice.lower() not in goods:
                            goods[prod_choice.lower()] = [products[prod_choice.lower()][1] * gramms / 100, gramms]
                            products[prod_choice.lower()][2] -= gramms
                            break
                        else:
                            goods[prod_choice.lower()][0] += products[prod_choice.lower()][1] * gramms / 100
                            goods[prod_choice.lower()][1] += gramms
                            products[prod_choice.lower()][2] -= gramms
                            break
                    else:
                        print('У нас есть только {}г. Введите еще раз.'.format(products[prod_choice.lower()][2]))
                        continue
            except KeyError:
                print('Вы указали неверный товар, попробуйте снова.')
    elif choice == 'n':
        break
    else:
        print('Вы ввели неверно, попробуйте еще раз.')
        continue
    print('Что-нибудь еще?\n'
          '1 - информация.\n'
          '2 - покупка.\n'
          'n - выход.')

pprint.pprint(products)
pprint.pprint(goods)
