'''
summ = 0
x = int(input('Введите ваше число: '))
for i in range(0, x + 1):
    if (i % 3) == 0:
        summ += i
        print('Число', i, 'делится на 3')
print('Сумма всех чисел делящихся на 3 без остатка:', summ)
'''

summ = 0
x = int(input('Введите ваше число: '))
y = 0
while y <= x:
    if y % 3 == 0:
        summ += y
        print(y)
    y += 1
print('Сумма чисел делящихся рна 3:', summ)
