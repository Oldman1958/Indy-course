"""
Программа запрашивает у пользователя курс доллара - вещественное число,
и также количество долларов (целое число), которое пользователь хочет приобрести.
В итоге программа должна вывести следующее сообщение:

Current dollar rate is <курс доллара>. You want to buy <количество долларов> dollars
You must pay <стоимость>
"""

rate = float(input())
want = int(input())
print(f'''Current dollar rate is {rate}. You want to buy {want} dollars''')
print(f'''You must pay {rate * want}''')
