# Задача №2
# Перемножить все нечётные значения в диапазоне от 1 до 100.

pr = 1
for i in range(1, 101):
    if i % 2 != 0:                                      # проверка на нечетность
        pr *= i
print(pr)
