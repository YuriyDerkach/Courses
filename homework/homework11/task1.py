# Простейший калькулятор c введёнными двумя
# числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа.
# Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы
# (сделать как отдельную операцию).

def inputArgument(arg):
    try:
        inputResult = float(input(arg))
    except ValueError:
        print('Число введено неверно. Попробуйте еще раз')
        inputArgument(arg)
    else:
        return inputResult

def operationChoice():
    operations = ('+', '-', '*', '/',)
    inputResult = input('Выберите операцию {}: '.format(operations))
    if inputResult in operations:
        return inputResult
    else:
        print('Операция введена неверно. Попробуйте еще раз')
        operationChoice()

def calculating(firstNum, secondNum, op):
    if op == '+':
        return firstNum + secondNum
    elif op == '-':
        return firstNum - secondNum
    elif op == '*':
        return firstNum * secondNum
    elif op == '/':
        try:
            return firstNum / secondNum
        except ZeroDivisionError:
            return 'бесконечность'

def calculatorExit(choise):
    if choise == 'y':
        return False
    elif choise == 'n':
        return True
    # проверка на то, какая буква "у" была введена (англ или рус)
    elif choise == 'у':
        calculatorExit(input('Вы ввели русскую букву "у", вместо английской.'))
    else:
        calculatorExit(input('Введите пожалуйста "y" или "n".'))

if __name__ == '__main__':
    repeat = True
    while repeat:
        firstArgument = inputArgument('Первое число: ')
        operation = operationChoice()
        secondArgument = inputArgument('Второе число: ')
        result = calculating(firstArgument, secondArgument, operation)

        print('Ответ:', result)

        repeat = calculatorExit(input('Продолжить? (y/n) '))
