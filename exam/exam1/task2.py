# 2. С клавиатуры вводится текст, определить, сколько в нём гласных, а сколько
# согласных. В случае равенства вывести на экран все гласные буквы.

while True:
    input_text = input('Введите текст: ')
    if input_text.isalpha():
        break
    else:
        print('Вы ввели неверно, попробуйте еще раз.')

vowel = 'eyuioaEYUIOAёуеыаоэяиюЁУЕЫАОЭЯИЮ'
consonant_sum = 0
vowel_sum = 0

for i in input_text:
    if i in vowel:
        vowel_sum += 1
    else:
        consonant_sum += 1

print('В {} {} гласных и {} согласных.'.format(input_text, vowel_sum, consonant_sum))

if vowel_sum == consonant_sum:
    print('Гласные буквы:', end=' ')
    for i in input_text:
        if i in vowel:
            print(i, end=' ')
