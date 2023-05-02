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
if list_str[0] == 'a' and list_str[1] == 'b' and list_str[2] == 'c':
    list_str[0], list_str[1], list_str[2] = 'w', 'w', 'w'
    print(''.join(list_str))
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
print('YES' if '@' and '.' in email else 'NO')
