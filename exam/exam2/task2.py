import random

# 2. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.

rand_list = [random.randint(0, 9) for _ in range(10)]
print(rand_list)

numbers_set = set(rand_list)

for number in numbers_set:
    print('{} имеет {} пар.'.format(number, rand_list.count(number) // 2))
