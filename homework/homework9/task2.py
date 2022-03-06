from task1 import number_input, error_analysis

# Задача №2
# Ввод с клавиатуры. Если строка введённая с клавиатуры – это числа, то поделить первое на
# второе. Обработать ошибку деления на ноль. Если второе число 0, то программа
# запрашивает ввод чисел заново. Также если были введены буквы, то обработать
# исключение.

first_number = number_input('First number = ')

while True:
    second_number = number_input('Second number = ')
    try:
        result = first_number / second_number
    except ZeroDivisionError as err:
        error_analysis(err)
    else:
        break

print(result)
