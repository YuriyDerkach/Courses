import random

# Задача №5
# Записать в массив все числа в диапазоне от 1 до 500 кратные 5.

new_arr_5 = []
arr_5 = []
for i in range(10):                                     # цикл для записи в список 10 случайных цифр
    arr_5.append(random.randint(1, 9))                  # от 1 до 9
print(arr_5)
for i in arr_5:
    if arr_5.count(i) >= 2:                             # если кол-во цифр i больше или равно 2, то
        new_arr_5.append(i)                             # записывает i в список new_arr_5
print(new_arr_5)
