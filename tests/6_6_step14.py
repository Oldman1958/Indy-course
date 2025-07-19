"""
Переменная countries содержит информацию о странах и трёх крупнейших городах в каждой из них.
Данные представлены в виде словаря, где ключами являются названия стран, а значениями — списки городов.

На вход программе будет подаваться название города, сохраняемое в переменную city.
Ваша задача — определить, к какой стране принадлежит введённый город.

Если страна успешно найдена, необходимо вывести сообщение следующего вида:

INFO: <City> is a city in <Country>
Если город не принадлежит ни одной из стран, указанных в словаре, выводится сообщение:

ERROR: Country for {City} not found
Обратите внимание: программа чувствительна к регистру букв,
поэтому ввод должен точно совпадать с написанием названий городов в словаре.
"""

countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()
for key, values in countries.items():
    if city in values:
        print(f'INFO: {city} is a city in {key}')
        break
else:
    print(f'ERROR: Country for {city} not found')
