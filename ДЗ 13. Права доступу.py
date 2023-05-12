# Это какой-то п....ц

list_oper = {'read': 'R',
             'write': 'W',
             'execute': 'X'
             }

quantity_files = int(input('Введите количество ваших файлов: '))
print('Возможные операции с файлами:', 'W - write', 'R - read', 'X - execute', sep='\n')
files = {}
for i in range(quantity_files):
    files_name, *file_type = input('Название файла, через пробел возможные операции с файлом: ').split(' ')
    files[files_name] = set(file_type)
print(files, sep='\n')

quantity_operation = int(input('Количество запросов к файлам: '))
finish_list = []
for q in range(quantity_operation):
    if list_oper[input('Желаемая операция с файлом: ')] in files[input('Название файла: ')]:
        finish_list.append('OK')
    else:
        finish_list.append('Access denied')
print('\n'.join(finish_list))
