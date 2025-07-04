"""
Создайте две переменные empty и empty_too, присвойте им значение None.

Затем выполните две проверки:

Выведите True, если обе переменные указывают на один и тот же объект в памяти, иначе False.

Выведите True, если переменные указывают на разные объекты, иначе False.
"""

empty = None
empty_too = None
print(empty is empty_too)
print(empty is not empty_too)
