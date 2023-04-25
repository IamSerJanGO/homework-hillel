# p.s. Я вообще в шоке как этот топорный код заработал !!!


x = int(input('Enter number:'))
z = x * '*'
print('1)')
for num1 in range(1, x + 1):
    print(z)
    z = (x - num1) * '*'

print('2)')

z = '*'
n = 1
for num2 in range(1, x + 1):
    print(z)
    n += 1
    z = n * '*'

print('3)')

z = x * '*'
c = ' '
for num3 in range(1, x + 1):
    print(z)
    z = (c * num3) + ((x - num3) * '*')


print('4)')

z = '*'
c = ' '
for num4 in range(1, x + 1):
    c = (x - num4) * ' '
    z = num4 * '*'
    print(c + z)
