import random

# 6. Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в
# первом списке, так и во втором.

nums_1 = [random.randint(0, 9) for _ in range(10)]
nums_2 = [random.randint(0, 9) for _ in range(10)]
print(nums_1)
print(nums_2)

print(len(set(nums_1) & set(nums_2)))
