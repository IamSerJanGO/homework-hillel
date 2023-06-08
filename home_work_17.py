def change():
    print('Введите элементы спистка через пробел !')
    user_lst = input().split()
    copy_lst = user_lst.copy()
    first, last = copy_lst[0], copy_lst[-1]
    if len(user_lst) >= 2:
        user_lst[0], user_lst[-1] = last, first
        print(f'Ваш измененный список: {user_lst}')
    else:
        print('Ваш список слишком короткий !')


change()

def to_dict():
    lst = input('Введите элементы спистка через пробел !: ').split()
    dictionary = {}
    for item in lst:
        dictionary[item] = item
    return dictionary


print('Словарь из вашего списка:', to_dict())

def sum_range(start: int, end: int):
    count = 0
    if start > end:
        start, end = end, start  # swap the value
    for i in range(start, end + 1):
        count += i
    return count


start = int(input('Enter your first number: '))
end = int(input('Enter your second number: '))
result = sum_range(start, end)
print(result)
