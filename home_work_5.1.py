summ = 0
x = int(input('Введите ваше число: '))
for i in range(0, x + 1):
    if (i % 3) == 0:
        summ += i
        print('Число', i, 'делится на 3')
print('Сумма всех чисел делящихся на 3 без остатка:', summ)
