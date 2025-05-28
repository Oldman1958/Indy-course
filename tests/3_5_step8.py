"""
Перепишите программу ниже при помощи elif, устранив тем самым вложенность условий

age = int(input())
member = bool(int(input()))

if age > 18:
    if member:
        print("Цена билета 75")
    else:
        print("Цена билета 100")
else:
    if member:
        print("Цена билета 25")
    else:
        print("Цена билета 50")
"""

age = int(input())
member = bool(int(input()))

if member and age > 18:
    print("Цена билета 75")
elif age > 18:
    print("Цена билета 100")
elif member:
    print("Цена билета 25")
else:
    print("Цена билета 50")