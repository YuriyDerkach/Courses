# 3.Ведьмаку заплатите чеканной монетой
# Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево,
# к тому же ведьмак не принимает купюры, он принимает только чеканные монеты.
# В мире ведьмака существуют монеты с номиналами 1, 5, 10, 25.
# Напишите программу, которая определяет какое минимальное количество чеканных монет нужно заплатить ведьмаку.
# Пример:
# На вход подается число 49.Ответом будет 7(25 + 10 + 10 + 1 + 1 + 1 + 1) те минимальное количество монет)

# списоки возможных номиналов монет и необходимых для оплаты монет
coins = [25, 10, 5, 1]
coins_to_pay = []
# ввод суммы для оплаты
payment = int(input())
# основной цикл берет номинал монеты, начиная с большей
for i in coins:
    while payment != 0:
        # проверка на возможность оплаты данным номиналом монеты
        # если да, то данный номинал записывается в список для оплаты и отнимается от общей суммы
        if payment >= i:
            coins_to_pay.append(i)
            payment -= i
        # иначе, прерывается второй цикл и берется следующий номинал
        else:
            break
# вывод кол-ва и номиналы затраченных монет
print(len(coins_to_pay), coins_to_pay)
