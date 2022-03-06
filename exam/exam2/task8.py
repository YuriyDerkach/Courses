import random

# 8. В текстовый файл построчно записаны фамилия и имя учащихся класса и его
# оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3
# баллов и посчитать средний балл по классу

students_tuple = ('Петр Петров', 'Иван Иванов', 'Николай Николаев', 'Андрей Андреев', 'Федор Федоров',)

with open('students_marks.txt', 'w+') as stud_marks:
    for student in students_tuple:
        stud_marks.write(student + ' ' + str(random.randint(0, 5)) + '\n')

with open('students_marks.txt', 'r') as stud_marks:
    stud_list = stud_marks.readlines()
print(stud_list)
marks = []

for line in stud_list:
    marks.append(line.replace('\n', '').split(' '))
print(marks)

sum_marks = 0

for student in marks:
    sum_marks += student[2]
    if int(student[2]) < 3:
        print(' '.join(student))

average = sum_marks / len(marks)

print('Средний балл по классу = {}'.format(average))
