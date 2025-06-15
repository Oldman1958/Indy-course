"""
В вашем распоряжении имеется список names.

На основании его при помощи генератора списков создайте новый список,
в котором каждый элемент создается по шаблону

My name is <имя>
Полученный список выведите на экран.
"""

names = ['Alice', 'Bob', 'Marry', 'Joe', 'Hilary', 'Stevia', 'Dylan', 'Kevin', 'Darvin']
new_names = [f'My name is {name}' for name in names]
print(new_names)
