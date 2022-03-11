import random
import string

# Если в функцию передается кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нем.
# Число - кол-во нечетных цифр
# Строка - кол-во букв
# Сделать проверку со всеми этими случаями.

def value_generator(value):
    if value == 'word':
        word = random.choice(string.ascii_uppercase)
        for step in range(random.randint(3, 9)):
            word += random.choice(string.ascii_lowercase)
        return word
    elif value == 'number':
        return str(random.randint(0, 1000))

def collection_generator(collect):
    values = ('word', 'number',)
    for step in range(random.randint(4, 10)):
        collect.append(value_generator(random.choice(values)))
    return collect

def result(collect):
    def word_len(word):
        print('{} имеет {} букв.'.format(word, len(word)))

    if type(collect) == tuple:
        for value in collect:
            if value.isalpha():
                word_len(value)
    elif type(collect) == list:
        words_count = 0
        numbers_count = 0
        for value in collect:
            if value.isalpha():
                words_count += 1
                word_len(value)
            elif value.isdigit():
                numbers_count += 1
                full_number = value.split()
                odd = 0
                for number in full_number:
                    if int(number) % 2 != 0:
                        odd += 1
                print('{} имеет {} нечетных цифр.'.format(value, odd))
        print('\nТакже в данном списке:\n'
              'Количество слов - {}.\n'
              'Количество чисел - {}.'.format(words_count, numbers_count))

if __name__ == '__main__':
    collections_types = ('список', 'кортеж',)
    type_choice = random.choice(collections_types)

    if type_choice == 'список':
        generated_collection = collection_generator(list())
    elif type_choice == 'кортеж':
        generated_collection = tuple(collection_generator(list()))

    print('Сгенерированная коллекция: {} {}.\n'.format(type_choice, generated_collection))
    result(generated_collection)
