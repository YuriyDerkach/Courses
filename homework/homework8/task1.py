# 1. Имеется список с произвольными данными. Поставлена задача преобразовать его в множество.
# Если какие-то элементы не неизменяемые, то пропускаем их. Вывести на экран полученное множество
# #дз

start_list = ['a', 'b', 2, 12, True, '213', 'True', False,
              {'a': 1, 'b': 2},
              [True, 1,
               (12, 13, 'a',),
               4],
              {'a', 'b', 4},
              (12, 'b',),
              False, '4', 'b'
              ]
print(start_list)

wrong_types = (set, list, dict,)
result_set = set()

for value in start_list:
    if type(value) not in wrong_types:
        result_set.add(value)

print(result_set)
