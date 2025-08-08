"""
Даны два списка чисел.

Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.
"""

set_1 = set(map(int, input().split()))
set_2 = set(map(int, input().split()))
out = sorted(set_1.intersection(set_2))
for i in out:
    print(i, end=' ')
