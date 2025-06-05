"""
Программа принимает на вход одно натуральное число и выводит на экран минимальную и максимальную цифры данного числа
в отдельных строчках.
"""

n = int(input())
maximum = 0
minimum = 9
while n > 0:
    last = n % 10
    if last > maximum:
        maximum = last
    if last < minimum:
        minimum = last
    n = n // 10
print(minimum)
print(maximum)
