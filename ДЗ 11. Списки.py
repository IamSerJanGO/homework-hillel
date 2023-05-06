print('Условие 1 и 2)')
# Первое и второе условие:
digit_list = []
x = 0
while x < 5:
    user_numb = input()
    if user_numb.isdigit():
        digit_list.append(user_numb)
        x += 1
print(digit_list)
digit_list.pop()
print('2)', digit_list, sep='\n')

# Третье условие:
print('Условие 3)')
digit_list2 = []
x = 0
while x < 10:
    user_numb2 = input()
    if user_numb2.isdigit():
        digit_list2.append(user_numb2)
        x += 1
search_numb = input('Enter your search number: ')
print(digit_list2.count(search_numb))
# Условие № 4

print('Условие 4)')
len_user_list = int(input('Enter your list length: '))
user_list = []
x = 0
while x < len_user_list:
    list_element = input()
    if list_element.isdigit():
        user_list.append(list_element)
        x += 1
user_list.reverse()
print(user_list)
# Условие № 5

print('Условие 5)')
list_1 = []
list_2 = []
x = 0
while x < 5:
    user_numb = input()
    if user_numb.isdigit():
        list_1.append(user_numb)
        x += 1
for i in list_1:
    if int(i) > 5:
        list_2.append(i)
print(list_2)

# Условие № 6
print('Условие 6)')
len_list = int(input())
user_list = []
x = 0
while x < len_list:
    element_list = input()
    if element_list.isdigit():
        user_list.append(int(element_list))
        x += 1
max_element = min_element = user_list[0]
for i in range(1, len(user_list)):
    if user_list[i] < min_element:
        min_element = user_list[i]
    elif user_list[int(i)] > max_element:
        max_element = user_list[i]
print(max_element, min_element, sep='\n')

# Условие № 7
print(' Условие 7)')
user_text = input('Enter your text: ')
x = 0
# list(user_text)
for i in list(user_text):
    if i.isdigit():
        x += 1
print(f'Кол-во цифр в тексте: {x}')
