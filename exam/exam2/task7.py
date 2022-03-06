# 7. Напишите программу, демонстрирующую работу try\except\finally

d = {'a': 1, 'b': 2, 'c': 3}

while True:
    k = input('input key ')
    try:
        print(d[k])
        break
    except KeyError:
        print('exception')
    finally:
        print('finally')
