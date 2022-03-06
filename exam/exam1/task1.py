# 1. С клавиатуры вводится 7 значное число. Если четных цифр в нем больше, чем
# нечетных, то найти сумму всех его цифр, если нечетных больше, то найти
# произведение 1 3 и 6 цифры.

while True:
    num = input('Введите семизначное число: ')
    if num.isdigit() and len(num) == 7:
        break
    else:
        print('Вы ввели неверно, попробуйте еще раз.')

num_list = []
for i in num:
    num_list.append(int(i))

even = 0         # чет

for i in num_list:
    if i % 2 == 0:
        even += 1

if len(num) - even < even:
    print('Сумма цифр = ', sum(num_list))
else:
    print('Произведение 1 3 и 6 цифры = ', num_list[0] * num_list[2] * num_list[5])
