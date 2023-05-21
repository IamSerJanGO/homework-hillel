# 1
from collections import Counter
import random

with open("exercise_1.txt", "r") as exercise_1:
    numbers = []
    for line in exercise_1:
        for word in line.split():
            if word.isdigit():
                numbers.append(int(word))
print(numbers)
# 2
text = input('Enter your text: ')
with open('data.txt', 'w') as data:
    data.write(text)
# 3
with open('numbers.txt', 'w') as numbers:
    numer = int(input('Kol-vo chisel: '))
    for i in range(numer):
        N = int(input('Chisla: '))
        numbers.write(str(N) + ' ')
# 4


numbers = [random.randint(-10000, 10000) for _ in range(100)]

with open('random_numbers.txt', 'w') as random_numbers:
    for numbers in numbers:
        random_numbers.write(str(numbers) + '\n')
# 5

with open("exercise_1.txt", "r") as exercise_1:
    char = 0
    for line in exercise_1:
        for word in line.split():
            if not word.isdigit():
                char += 1
print('Количество слов в вашем тексе:', char)
# 6
with open('numbers.txt', 'r') as numbers:
    integer = []
    for i in numbers:
        for dig in i.split():
            if dig.isdigit():
                integer.append(int(dig))

print(f'Сумма чисел в вашем тексте: {sum(integer)}')
# 7


with open('exercise_1.txt', 'r') as file:
    lines = file.readlines()

words = []
for line in lines:
    words.extend(line.split())

word_counts = Counter(words)
top_words = word_counts.most_common(5)

print("Топ 5 наиболее часто повторяющихся слов:")
for word, count in top_words:
    print(f"'{word}' - {count} раз(а)")
