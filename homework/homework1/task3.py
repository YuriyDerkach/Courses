# Задача №3
# Записать в массив все числа в диапазоне от 1 до 500 кратные 5.

arr = []
for i in range(1, 501):
    if i % 5 == 0:                                      # проверка на кратность 5
        arr.append(i)
print(arr)