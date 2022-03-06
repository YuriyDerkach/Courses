from time import localtime
from random import randint
import os

# Задача №1
# Матрица 5 х 5. Найти строку с максимальной суммой элементов и вывести её номер.

FILE_ABSPATH = os.path.abspath(__file__)

def error_analysis(error_info):
    error_date = '{}.{}.{} {}:{}:{}'.format(
        localtime().tm_mday,
        localtime().tm_mon,
        localtime().tm_year,
        localtime().tm_hour,
        localtime().tm_min,
        localtime().tm_sec,
    )
    print(FILE_ABSPATH, '\n', error_date, '\n', error_info)
    with open('error_logs.txt', 'a+') as error_logs:
        error_logs.write(FILE_ABSPATH +
                         '\nError date:\n' +
                         error_date +
                         '\nError info:\n' +
                         str(error_info) +
                         '\n' * 2
                         )

def number_input(part_of_matrix):
    while True:
        try:
            number = int(input(part_of_matrix))
        except ValueError as err:
            error_analysis(err)
        else:
            break
    return number

LINES = number_input('Lines = ')
COLUMNS = number_input('Columns = ')

matrix = list([0] * COLUMNS for _ in range(LINES))

for line in range(LINES):
    for column in range(COLUMNS):
        matrix[line][column] = randint(0, 9)
        print(matrix[line][column], end=' ')
    print()

max_sum_line = {'Sum': 0, 'Index': None}
all_max_sum_lines = []

for line in range(LINES):
    if sum(matrix[line]) > max_sum_line['Sum']:
        all_max_sum_lines.clear()
        max_sum_line = {'Sum': sum(matrix[line]), 'Index': line}
        all_max_sum_lines.append(max_sum_line)
    elif sum(matrix[line]) == max_sum_line['Sum']:
        all_max_sum_lines.append({'Sum': sum(matrix[line]), 'Index': line})

print('Max sum lines:')
for line in all_max_sum_lines:
    print('Index - {}, Sum = {}'.format(line['Index'], line['Sum']))

# но можно было и так сделать, но опять же, он выведет только одну строку, даже если максимальных несколько:
# max_sum_line = max(matrix, key=sum)
# print('Max sum line:')
# print('Index - {}, Sum = {}'.format(matrix.index(max_sum_line), sum(max_sum_line)))
