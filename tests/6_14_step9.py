"""
Даны два списка чисел. Выведите все числа в порядке возрастания,
которые входят в первый список, но при этом отсутствуют во втором.
"""

a = {int(i) for i in input().split()}
b = {int(i) for i in input().split()}
print(*sorted(a.difference(b)))
