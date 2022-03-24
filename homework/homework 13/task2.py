# Детская игра висилица. Аналог поле чудес, ток без барабана и секторов.
# Компьютер загадывает слово из списка слов, пользователь видит на экране
# это слово в виде звездочек за место букв и пытается угадать буквы,
# угаданная буква появляется вместо звездочки в слове. Можно усложнить наличием кол-ва попыток:)

import random

words_list = ('кострома', 'вольфсбург', 'павлово', 'вена', 'ленск', 'кардифф', 'александрия',)
selected_word = [letter for letter in random.choice(words_list)]
guess_word = ['*' for _ in range(len(selected_word))]
print(''.join(selected_word))

while selected_word != guess_word:
    print(''.join(guess_word))
    guess_letter = input('Введите букву:\n')
    if guess_letter.isalpha() and len(guess_letter) == 1:
        if guess_letter.lower() not in selected_word:
            print('Нет такой буквы.')
        for letter_index in range(len(selected_word)):
            if guess_letter.lower() == selected_word[letter_index]:
                guess_word[letter_index] = guess_letter.lower()
    elif guess_letter.lower() == ''.join(selected_word):
        break
    else:
        print('{} - не одна буква или не буква вообще.'.format(guess_letter))

print('Поздравляю! Вы отгадали слово!')
