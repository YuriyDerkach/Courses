# Задача №4
# Записать в массив все числа в диапазоне от 1 до 500 кратные 5.

for i in range(1, 498):
    if i % 2 == 0:                                      # проверка на четность
        print(i)
