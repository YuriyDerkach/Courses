# 6. Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в
# веденном с клавиатуры слове. (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а
# также сколько всего букв в слове, сколько гласных и согласных

while True:
    input_text = input('Введите текст без пробелов: ')
    if ' ' not in input_text:
        break
    else:
        print('Вы ввели неверно, попробуйте еще раз.')

upper_couple_count = 0
lower_couple_count = 0
only_letters = ''
vowel = 'eyuioaEYUIOAёуеыаоэяиюЁУЕЫАОЭЯИЮ'
consonant_sum = 0
vowel_sum = 0

for index in range(1, len(input_text)):
    if input_text[index].isalpha() and input_text[index - 1].isalpha():
        if input_text[index].isupper() and input_text[index - 1].isupper():
            upper_couple_count += 1
        elif input_text[index].islower() and input_text[index - 1].islower():
            lower_couple_count += 1

for index in input_text:
    if index.isalpha():
        only_letters += index
        if index in vowel:
            vowel_sum += 1
        else:
            consonant_sum += 1

print('В введенной строке {} пар верхнего и {} нижнего регистра, {} букв, из которых {} гласных и {} согласных.'
      .format(upper_couple_count, lower_couple_count, len(only_letters), vowel_sum, consonant_sum))
