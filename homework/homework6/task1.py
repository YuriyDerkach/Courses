import random

# Есть кортеж, например ('need', 'to', 'sleep', 'more'). Создать новый кортеж,
# который будет содержать вложенные кортежи, представляющие собой пары элементов из исходного,
# т.е. (('need', 'to'), ('to', 'sleep'), ('sleep', 'more'))
# Использовать для этого одну из встроенных функций.

ALPHA = 'qwertyuiopasdfghjklzxcvbnm'
case = ('upper', 'lower', 'number',)

rand_list = []
rand_word = []
pre_result_list = []
result_list = []

for word in range(random.randint(3, 10)):
    for letter in range(random.randint(2, 10)):
        rand_case = random.choice(case)
        if rand_case == 'upper':
            rand_word.append(random.choice(ALPHA.upper()))
        elif rand_case == 'lower':
            rand_word.append(random.choice(ALPHA))
        elif rand_case == 'number':
            rand_word.append(str(random.randint(0, 9)))
    rand_list.append(''.join(rand_word))
    rand_word.clear()

rand_tuple = tuple(rand_list)
print(rand_tuple)

first_list = [rand_tuple[1:]]
second_list = [rand_tuple[:-1]]

for first, second in zip(first_list, second_list):
    pre_result_list.append([first, second])

for nested_list in pre_result_list:
    result_list.append(tuple(nested_list))

result_tuple = tuple(result_list)
print(result_tuple)
