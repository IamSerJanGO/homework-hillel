def change(user_lst):
    copy_lst = user_lst
    first, last = copy_lst[0], copy_lst[-1]
    if len(user_lst) >= 2:
        user_lst[0], user_lst[-1] = last, first
        print(f'Ваш измененный список: {user_lst}')
    else:
        print('Ваш список слишком короткий !')


print('Введите элементы спистка через пробел !')
user_lst = input().split()
change(user_lst)


def to_dict(lst):
    dictionary = {}
    for item in lst:
        dictionary[item] = item
    return dictionary


lst = input('Введите элементы спистка через пробел !: ').split()
print('Словарь из вашего списка:', to_dict(lst))


def sum_range(start: int, end: int):
    if start > end:
        start, end = end, start  # swap the value
    return sum(range(start, end + 1))


start = int(input('Enter your first number: '))
end = int(input('Enter your second number: '))
result = sum_range(start, end)
print(result)
