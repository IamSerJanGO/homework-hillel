# Это какой-то п....ц

dikt_operation = {'read': 'R', 'write': 'W', 'execute': 'X'}  # Создаем словарь с возможными операциями и их сокращенным значениям

num_files = int(input('Введите количество ваших файлов: '))
for key, operation in dikt_operation.items():  # Выводим для пользователя возможные операции и их абривиатуры
    print(key, operation)
files = {}
for i in range(num_files):  # С помощью цикла создаем словарь с названием файлов и их возможными операциями
    files_name, *type_operation = input('Название файла, через пробел возможные операции с файлом: ').split()
    files[files_name] = set(type_operation)
# print(files, sep='\n')  # оставил для себя - удобно проверять код

num_operations = int(input('Количество запросов к файлам: '))  # Запрашиваем количество запросов к файлам
finish_list = []
for q in range(num_operations):  # С помощью цикла создаем и проверяем запросы пользователя
    desired_operation = input('Введите операцию: ')
    desired_file = input('Введите название файла: ')
    search_operation = dikt_operation.get(desired_operation)
    if search_operation and files.get(desired_file):  #
        if search_operation in files[desired_file]:  #
            finish_list.append('OK')
        else:
            finish_list.append('Access denied')
    else:
        finish_list.append('Invalid input')
print('\n'.join(finish_list))  # Выводим на экрвн готовый результат )))
