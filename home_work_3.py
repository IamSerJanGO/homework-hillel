from math import sqrt

x = int(input())
y = int(input())
z = int(input())
p = (x + y + z) / 2
S = sqrt(p * (p - x) * (p - y) * (p - z))
print(S)
