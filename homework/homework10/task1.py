import random

# Есть массив состоящий из слов и чисел, нужно записать в файл сначала
# слова в порядке их длины, а после слов цифры в порядке возрастания.

ALPHA = 'qwertyuiopasdfghjklzxcvbnm'
value_type = ('word', 'number',)
case = ('upper', 'lower',)

rand_words_list = []
rand_numbers_list = []
rand_word = []

for word in range(random.randint(3, 10)):
    rand_type = random.choice(value_type)
    if rand_type == 'number':
        rand_numbers_list.append(random.randint(0, 100))
    else:
        for letter in range(random.randint(2, 10)):
            rand_case = random.choice(case)
            if rand_case == 'upper':
                rand_word.append(random.choice(ALPHA.upper()))
            elif rand_case == 'lower':
                rand_word.append(random.choice(ALPHA))
        rand_words_list.append(''.join(rand_word))
        rand_word.clear()

sorted_list = sorted(rand_words_list, key=len) + sorted(rand_numbers_list)
result_list = []
for value in sorted_list:
    if type(value) != str:
        result_list.append(str(value))
    else:
        result_list.append(value)

print(result_list)

with open('newfile.txt', 'w+') as newfile:
    newfile.write(' '.join(result_list))
