from random import randint

# 4. Посчитать, сколько раз встречается определенная цифра в числах. Количество
# введенных чисел и искомая цифра задаются с клавиатуры. Числа выбираются
# рандомно.

while True:
    numbers_count = input('Введите кол-во чисел (не более 20): ')
    if numbers_count.isdigit() and len(numbers_count) <= 20:
        numbers_count = int(numbers_count)
        break
    else:
        print('Вы ввели неверно, попробуйте еще раз.')

while True:
    needed_number = input('Введите искомую цифру: ')
    if needed_number.isdigit() and len(needed_number) == 1:
        needed_number = needed_number
        break
    else:
        print('Вы ввели неверно, попробуйте еще раз.')

numbers_list = str([randint(0, 10000) for i in range(numbers_count)])
print(numbers_list)

needed_number_count = numbers_list.count(needed_number)
print('Цифра {} встречается {} раз.'.format(needed_number, needed_number_count))
