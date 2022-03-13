# Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше или равно длине слова, выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.

class Analyzer:

    def __init__(self, value):
        self.value = value
        self.vowel = 'eyuioaёуеыаоэяию'

    def processing(self):
        if self.value.isalpha():
            vowel = []
            consonants = []
            for letter in self.value:
                if letter.lower() in self.vowel:
                    vowel.append(letter)
                else:
                    consonants.append(letter)
            if len(vowel) * len(consonants) > self.value_len():
                return 'В {} {} согласных.'.format(self.value, len(consonants))
            else:
                return 'В {} {} гласных.'.format(self.value, len(vowel))
        elif self.value.isdigit():
            even = []
            for num in self.value:
                if int(num) % 2 == 0:
                    even.append(int(num))
            return sum(even) * self.value_len()
        else:
            return 'Введено неверно, попробуйте еще раз.'

    def value_len(self):
        return len(self.value)

if __name__ == '__main__':
    exit_methods = ('exit', 'выход',)
    while True:
        analyzer = Analyzer(input('Введите текст или число (для выхода введите exit или выход): '))
        if analyzer.value.lower() in exit_methods:
            break
        print(analyzer.processing())
