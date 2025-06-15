"""
Перепишите программу ниже при помощи генератора списков.

n = int(input())

result = []
for x in range(n + 1):
    if x % 2 == 0:
        result.append(x * x)
print(result)
"""

n = int(input())
result = [x * x for x in range(n + 1) if x % 2 == 0]
print(result)
