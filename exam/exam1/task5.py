# 5. Вводится строка, содержащая буквы, целые неотрицательные числа и иные символы.
# Требуется все числа, которые встречаются в строке отдельно вывести на экран. Строка
# может содержать пробелы.

input_text = input('')
new_string = ' '
prev_index = ''

for index in input_text:
    if index.isdigit() or index == ' ' and new_string[-1] != ' ':
        new_string += index
    elif prev_index.isdigit():
        new_string += ' '
    prev_index = index

print(new_string)

numbers_list = new_string.split(' ')
result_list = []

for index in numbers_list:
    if index.isdigit():
        result_list.append(index)

print(result_list)
