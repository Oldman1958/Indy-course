"""
Напишите самостоятельно программу, которая работает по этому сценарию
(https://pikabu.ru/story/kakoy_yazyik_programmirovaniya_stoit_uchit_pervyim_10747957)
и помогает пользователю определиться с языком программирования.

Как справитесь, поделитесь в комментариях с нами вашим решением.
"""

print("Программа выводит подходящий Вам язык программирования")
print()
print('На вопросы отвечайте Да или Нет')
print()
q = input("Хотите много зарабатывать?")
print()
if q.lower().strip() == 'да':
    q = input("Вы тупой?")
    if q.lower().strip() == "да":
        q = input('Очень?')
        if q.lower().strip() == "да":
            q = input("У Вас есть друзья?")
            if q.lower().strip() == "да":
                q = input("Они тоже тупые?")
                if q.lower().strip() == "да":
                    print("JavaScript")
                else:
                    print("Ruby")
            else:
                print("PHP")

        else:
            q = input('Вы насмотрелись уроков Хауди Хо?')
            if q.lower().strip() == "да":
                print('Python')
            else:
                q = input('Вам нравится Windows?')
                if q.lower().strip() == "да":
                    print('C#')
                else:
                    q = input('Вы гей?')
                    if q.lower().strip() == "да":
                        print('Swift')
                    else:
                        print("Perl")

    else:
        q = input("Вы инженер?")
        if q.lower().strip() == "да":
            q = input("Вам больше 50?")
            if q.lower().strip() == 'да':
                print('Fortran')
            else:
                print('MatLab')
        else:
            q = input("У Вас есть ноги?")
            if q.lower().strip() == "да":
                q = input("А они Вам нужны?")
                if q.lower().strip() == "да":
                    print('Java')
                else:
                    print("C++")
            else:
                print("C")
else:
    print('Delphi')
