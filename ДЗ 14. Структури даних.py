# Первое условие !
july = {'Nik', 'Ivan', 'Sema', 'Vova', 'Sasha', 'Tolik', 'Alex', 'Kolya', 'Andrey'}
june = {'Max', 'Artem', 'Jenya', 'Nikita', 'Kirill', 'Nik', 'Ivan', 'Sema', 'Vova'}
print(f'Имена должников за июль и за июнь: {",".join(july.intersection(june))}')
print(f'Должники за Июль у которых нет долга за Июнь: {",".join(july.difference(june))}')

# Второе условие
# test_list = ['ListTest', 'SerJan', 'GoogleDisk']
# new_list = []

# for object_list in test_list:
#     str_object = ''
#     for i in range(len(object_list)):
#         if object_list[i].isupper():
#             if i != 0:
#                 str_object += '_'
#             str_object += object_list[i].lower()
#         else:
#             str_object += object_list[i]
#     new_list.append(str_object)
# print(new_list)

#  Второе условие (Вариант второй)
test_list, new_list = ['ListTest', 'SerJan', 'GoogleDisk'], []

for num_list, object_list in enumerate(test_list):
    str_ob = ''
    for i, char in enumerate(object_list):
        if char.isupper():
            if i != 0:
                str_ob += '_'
            str_ob += char.lower()
        else:
            str_ob += char
    new_list.append(str_ob)
print(new_list)
