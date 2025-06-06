"""
Даны два натуральных числа A и B. Требуется найти их наименьшее общее кратное (НОК).
"""

a, b = map(int, input().split())
n, k = a, b
c = 0

while b > 0:
    c = a % b
    a = b
    b = c
nod = a
nok = int((n * k) / nod)
print(nok)
