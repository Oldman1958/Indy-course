"""
Создайте список первых букв каждого слова строки, хранящейся в переменной phrase,
и выведите его на экран.

Сама переменная phrase определяется во входных данных, вам вводить ничего не нужно.
"""

st = 'Create a list of the first letters of every word in this string'
a = st.split(' ')
print([i[0] for i in a])
