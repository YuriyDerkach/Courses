import random

# Казино. Компьютер генерирует числа от 1 до 10 и от 1 до 2-х соответственно.
# Цифры от одного до 10 отвечают за номера, а от 1 до 2 за цвета(1-красный,2 черный).
# Пользователю дается 5 попыток угадать номер и цвет (Прим. введения с клавиатуры: 3 красный).
# В случае неудачи вывести на экран правильную комбинацию.

# --------------------------------------------------------------------------------------------------------
# Без подсказок
# --------------------------------------------------------------------------------------------------------

colors = ['red', 'black']

rand_color = random.choice(colors)
rand_num = random.randint(1, 10)

# print(rand_num, rand_color)               # Для проверки

while True:
    inp_color = input('Color (red or black) = ')
    if inp_color == 'red' or inp_color == 'black':
        break
    else:
        print(f'{inp_color} is not red or black! Please try again!')

while True:
    inp_num = int(input('Number (from 1 to 10) = '))
    if inp_num > 0 and inp_num < 11:
        break
    else:
        print(f'{inp_num} is out of range (from 1 to 10)! Please try again!')

if inp_color == rand_color and inp_num == rand_num:
    print('You win!')
else:
    print('You lose!')

# --------------------------------------------------------------------------------------------------------
# С подсказками
# --------------------------------------------------------------------------------------------------------

colors = ['red', 'black']

rand_color = random.choice(colors)
rand_num = random.randint(1, 10)
_try = 5

# print(rand_num, rand_color)               # Для проверки
print(f'You have {_try} try!')

while _try > 0:
    inp_num = int(input('Number (from 1 to 10) = '))
    if inp_num > 0 and inp_num < 11:
        if inp_num > rand_num:
            while True:
                choice = input('Your number may be more than random. Do you want continue?(y/n): ')
                if choice != 'y' and choice != 'n':
                    print(f'{choice} is not y or n! Please try again!')
                else:
                    break
            if choice == 'n':
                _try -= 1
                print(f'Now you have {_try} try!')
                continue
            else:
                break
        elif inp_num < rand_num:
            while True:
                choice = input('Your number may be less than random. Do you want continue?(y/n): ')
                if choice != 'y' and choice != 'n':
                    print(f'{choice} is not y or n! Please try again!')
                else:
                    break
            if choice == 'n':
                _try -= 1
                print(f'Now you have {_try} try!')
                continue
            else:
                break
        else:
            break
    else:
        print(f'{inp_num} is out of range (from 1 to 10)! Please try again!')

if _try == 0:
    while True:
        inp_color = input('Color (red or black) = ')
        if inp_color == 'red' or inp_color == 'black':
            break
        else:
            print(f'{inp_color} is not red or black! Please try again!')
else:
    while _try > 0:
        inp_color = input('Color (red or black) = ')
        if inp_color == 'red' or inp_color == 'black':
            if inp_color != rand_color:
                while True:
                    choice = input('Your color may be wrong. Do you want continue?(y/n): ')
                    if choice != 'y' and choice != 'n':
                        print(f'{choice} is not y or n! Please try again!')
                    else:
                        break
                if choice == 'n':
                    _try -= 1
                    print(f'Now you have {_try} try!')
                    continue
                else:
                    break
            else:
                break
        else:
            print(f'{inp_color} is not red or black! Please try again!')

if inp_color == rand_color and inp_num == rand_num:
    print('You win!')
else:
    print('You lose!')
