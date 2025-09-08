"""
Напишите функцию print_initials(name, surname, middlename), которая принимает три параметра:

name – имя человека;

surname – фамилия человека;

middlename– отчество человека;
а затем выводит на печать фамилию и инициалы в определенном формате (первая буква фамилии должна стать заглавной,
все остальные строчные; в имени и отчестве остаются только по одной букве в верхнем регистре).

Ваша задача — написать только определение функции print_initials. Вызов функции делать не нужно!
"""


# объявление функции
def print_initials(name, surname, middlename):
    name = name.lower().title()
    surname = surname.lower().title()
    middlename = middlename.lower().title()
    print(f'{surname} {name[0]}.{middlename[0]}.')


# считываем данные
name = input()
surname = input()
middlename = input()

# вызываем функцию
print_initials(name, surname, middlename)
