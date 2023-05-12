# Это какой-то п....ц

dikt_operation = {'read': 'R', 'write': 'W', 'execute': 'X'}

num_files = int(input('Введите количество ваших файлов: '))
for key, operation in dikt_operation.items():
    print(key, operation)
files = {}
for i in range(num_files):
    files_name, *type_operation = input('Название файла, через пробел возможные операции с файлом: ').split('')
    files[files_name] = set(type_operation)
# print(files, sep='\n') - оставил для себя - удобно проверять код

num_operations = int(input('Количество запросов к файлам: '))
finish_list = []
for q in range(num_operations):
    if dikt_oper[input('Желаемая операция с файлом: ')] in files[input('Название файла: ')]:
        finish_list.append('OK')
    else:
        finish_list.append('Access denied')
print('\n'.join(finish_list))
