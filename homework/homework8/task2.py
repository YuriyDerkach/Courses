from random import randint

# 2. Предоставлен список натуральных чисел. Требуется сформировать из них множество.
# Если какое-либо число повторяется, то преобразовать его в строку по образцу: например,
# если число 4 повторяется 3 раза, то в множестве будет следующая запись: само число 4,
# строка «44» (второе повторение, т.е. число дублируется в строке),
# строка «444» (третье повторение, т.е. строка множится на 3).
# #дз_со_звездочкой

rand_list = [str(randint(1, 9)) for _ in range(20)]
print(rand_list)

numbers_set = set(rand_list)
result_set = numbers_set.copy()
print(numbers_set)
print(result_set)

for number in numbers_set:
    if rand_list.count(number) > 1:
        for factor in range(2, rand_list.count(number) + 1):
            result_set.add(number * factor)

print(result_set)
