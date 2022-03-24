# 1. Симулятор лифта. Суть в следующем, изначально консоль выдает сообщение,
# что вы на 1 этаже (этажность придумываете сами) и предлагает ввести цифру этажа,
# чтобы подняться, во время подема мы видим в принте проезжающие этажи (цифры).
# Доехав до нужного, мы получаем сообщение, где находимся и вновь
# (и так бесконечно или до кодового слова) мы можем спуститься или подняться на
# нужный этаж. В общем лифтик. Сложность еще и в том, что мы не можем опуститься
# ниже первого или подняться выше 10го (если в здании 10 этажей)

from random import randint
from time import sleep

on_level = 1
levels = [level + 1 for level in range(randint(5, 9))]
print(levels)

while True:
    print('Вы сейчас на {} этаже'.format(on_level))
    try:
        to_level = int(input('Выберите этаж (1 - {}):\n'.format(levels[-1])))
    except ValueError:
        print('Неверно!')
        continue

    if to_level not in levels or to_level == on_level:
        continue

    sleep(1)
    print('Двери закрылись')

    while on_level != to_level:
        if to_level < on_level:
            sleep(3)
            on_level -= 1
            print('{} этаж.'.format(on_level))
        elif to_level > on_level:
            sleep(3)
            on_level += 1
            print('{} этаж.'.format(on_level))

    sleep(1)
    print('Двери открылись')
