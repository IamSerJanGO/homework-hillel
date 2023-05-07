
# Первое условие
first_word = input('Enter your word: ')
print('+' if first_word == first_word[::-1] else '-')

# Второе условие
user_text = input('Enter yout text: ')
user_word = input('What word are you looking for ?')
print('Yes' if user_word in user_text else 'No')

# Третье условие
user_str = input('Enter your text:')
list_str = list(user_str)
if user_str.startswith('abc'):
    user_str = 'www' + user_str[3:]
    print(user_str)
else:
    user_str += 'qqq'
    print(user_str + 'qqq')
# Условие № 4
new_str = list(input('Введите выш текст:'))
no_dgs_str = []
for del_dgs in new_str:
    if not del_dgs.isdigit():
        no_dgs_str.append(del_dgs)
print(''.join(no_dgs_str))

# Условие № 5
email = input('Введите вашу почту: ')
print('YES' if '@' in email and '.' in email else 'NO')
