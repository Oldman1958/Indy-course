"""
Программа получает на вход натуральное число N.
Нужно найти количество его делителей.
"""

n = int(input())
a = 1
count = 0
while a * a <= n:
    if n % a == 0 and a * a != n:
        count += 2
    elif n % a == 0 and a * a == n:
        count += 1
    a += 1

print(count)
