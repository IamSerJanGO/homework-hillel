"""
Я попробую сделать проверку пароля на три уровння сложности (да простит меня моя мышка и соседи по квартире)
Дан ряд условий:
1. Пароль должен быть не менее 10-ти символов в длину - ОБЯЗАТЕЛЬНОЕ УСЛОВИЕ
2. Пароль должен содержать минимум один символ верхнего регистра - ОБЯЗАТЕЛЬНОЕ УСЛОВИЕ
3. Пароль должен содержать минимум один символ нижнего регистра - ОБЯЗАТЕЛЬНОЕ УСЛОВИЕ
4. Пароль может содержать один и более специальный символ: !  ^  ?  ,  .  +  =  % НЕОБЯЗАТЕЛЬНОЕ УСЛОВИЕ !!!
5. Пароль может содержать одну и более цыфр - НЕОБЯЗАТЕЛЬНОЕ УСЛОВИЕ !!!
"""
# Ну что ? Поехали ?
# Надеюсь доедем ....)))

password = input('Введите пароль: ')
x = 0  # Переменная для длины пароля
z1, z2, y1, y2 = 0, 0, 0, 0  # Две переменные "z" для обязательных условий, и две переменные "у" для необязательных
# условий
if len(password) >= 10:
    ...
else:
    exit('Прости, но пароль слишком короткий)')
if len(password) >= 15:
    x = 1
for i in password:
    if i.isupper():
        z1 = 1  # первая переменная для обязательных условий
    if i.islower():
        z2 = 1  # вторая переменная для обязательных условий
    if i == '_' or i == '!' or i == '^' or i == ',' or i == '.' or i == '?' or i == '+' or i == '=' or i == '%':
        y1 = 1  # первая переменная для необязательных условий
    if i.isdigit():
        y2 = 1  # вторая переменная для необязательных условий
if z1 == 1 and z2 == 1:
    if x == 1 and y1 == 1 and y2 == 1:  #
        print('Отлично ! Пароль очень надежный!')
    elif x == 1 and y1 == 1 or x == 1 and y2 == 1:
        print('Неплохо ! Пароль среднец надежности')
    elif y1 == 1 or y2 == 1:
        print('Пароль слабый, но ты сам отвечаешь за свою безопасность)')
else:
    exit('Пароль слишком легкий - введите новый пароль')
