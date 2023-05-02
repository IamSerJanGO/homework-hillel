password = input('Введите пароль: ')
pass_length = pass_upp = pass_low = pass_digits = special_char = False
special_char_list = '!@#$%^&*+=_'
password_score = 0
if len(password) >= 8:
    pass_length = True
    password_score += 1
for i in password:
    if i.islower():
        pass_low = True
    if i.isupper():
        pass_upp = True
    if i.isdigit():
        pass_digits = True
    if i in special_char_list:
        special_char = True
password_score += sum((pass_low, pass_upp, pass_digits, special_char))
print(f'password_score: {password_score}')
if pass_length is False:
    print('The minimum password length is 8')
if pass_low is False:
    print('Use lower letters')
if pass_upp is False:
    print('Use capital letters')
if pass_digits is False:
    print('Use digits')
if special_char is False:
    print('Use special characters')
