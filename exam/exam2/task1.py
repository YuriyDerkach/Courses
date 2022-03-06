import random

# 1. Дан список. Выведите те его элементы, которые встречаются в списке только один
# раз. Элементы нужно выводить в том порядке, в котором они встречаются в
# списке.

rand_list = [random.randint(0, 9) for _ in range(20)]
print(rand_list)

unique_numbers = []

for number in rand_list:
    if number not in unique_numbers and rand_list.count(number) == 1:
        unique_numbers.append(number)
        print(number, end=' ')
print()
