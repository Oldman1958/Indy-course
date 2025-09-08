"""
Напишите функцию is_between, которая принимает три аргумента и печатает True,
если первое число находится между двумя вторыми включительно, и False в противном случае.

Ваша задача — написать только определение функции is_between. Вызов функции делать не нужно!
"""


# объявление функции
def is_between(name, surname, middlename):
    if surname <= name <= middlename or surname >= name >= middlename:
        print("True")
    else:
        print("False")


# считываем данные
a, b, c = map(int, input().split())

# вызываем функцию
is_between(a, b, c)
