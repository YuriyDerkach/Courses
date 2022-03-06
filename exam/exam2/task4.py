# 4. Создайте словарь из строки 'An apple a day keeps the doctor away' следующим
# образом: в качестве ключей возьмите символы строки, а значениями пусть будут
# числа, соответствующие количеству вхождений данной буквы в строку.

st = 'An apple a day keeps the doctor away'

keys_set = set(st.lower())
keys_set.discard(' ')
print(keys_set)

st_dict = {}

for letter in keys_set:
    st_dict[letter] = st.count(letter)

print(st_dict)
