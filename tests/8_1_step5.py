"""
Перед вами пример реализации программы из предыдущего шага,
в которой имя человека поступает на вход программы и сохраняется в переменной person.

Ваша задача — переписать программу так, чтобы не возникало исключения KeyError.
"""

ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}

person = input()

age = 0

if person in ages:
    age = ages[person]

if age:
    print(f'{person} is {age} years old.')
else:
    print(f"{person}'s age is unknown.")
