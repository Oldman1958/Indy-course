"""
Перед вами словарь account.

Ваша задача — сохранить в виде кортежа все ключи из словаря account.
В качестве ответа необходимо вывести полученный  кортеж.

Сам словарь account определяется внутри входных данных,
поэтому считывать данные вам не требуется.
"""
account = {
    "id": 3136,
    "uid": "1359acc6-f07a-4a2a-984e-3fb809982948",
    "account_number": "0847799459",
    "iban": "GB90XTND56373623909314",
    "bank_name": "ABN AMRO HOARE GOVETT CORPORATE FINANCE LTD.",
    "routing_number": "126602476",
    "swift_bic": "BCYPGB2LHGB"
}
keys = list(account)
print(keys)
