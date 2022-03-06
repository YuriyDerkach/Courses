# 3. Даны два кортежа:
# C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# C_2 = (45, 21,124,76,5,23,91,234)
# Необходимо определить:
# 1) Сумма элементов какого из кортежей больше и вывести соответствующее
# сообщение на экран (Сумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных и максимальных элементов
# этих кортежей

C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
C_2 = (45, 21, 124, 76, 5, 23, 91, 234)

if sum(C_1) > sum(C_2):
    print('Сумма больше в кортеже - C_1')
else:
    print('Сумма больше в кортеже - C_2')


print('Для С_1 макс. число - {} и имеет индекс {}.'.format(max(C_1), C_1.index(max(C_1))))
print('Для С_1 мин. число - {} и имеет индекс {}.'.format(min(C_1), C_1.index(min(C_1))))
print('Для С_2 макс. число - {} и имеет индекс {}.'.format(max(C_2), C_2.index(max(C_2))))
print('Для С_2 мин. число - {} и имеет индекс {}.'.format(min(C_2), C_2.index(min(C_2))))
