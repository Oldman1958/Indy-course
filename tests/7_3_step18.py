"""
Ваша задача написать функцию get_domain_name, которая принимает строку url,
извлекает из нее доменное имя и возвращает его в качестве строки

get_domain_name("http://google.com") => "google"
get_domain_name("http://google.co.jp") => "google"
get_domain_name("www.xakep.ru") => "xakep"
get_domain_name("https://youtube.com") => "youtube"
get_domain_name("https://www.asos.com") => "asos"
get_domain_name("http://www.lenovo.com") => "lenovo"


Строка url может начинаться с протоколов http://  https:// или с www. URL, начинающиеся с протоколов http://  https://,
могут также содержать www.

Ваша задача - написать только определение функции get_domain_name
"""


def get_domain_name(url):  # объявляем функцию, которая принимает url-адрес
    if '//' in url:  # если в адресе есть 2 символа '/', то...
        a = url.split('//')  # мы в переменную сохраняем адрес разбитый на список по разделителю '//'
        if 'www' in a[
            1]:  # дальше проверяем есть ли в разделенном адресе после символов //, комбинация www, если есть, то ...
            a[1] = a[1].split('.')  # ту часть, которая после символов //, разбиваем ещё и по разделителю точка
            return a[1][
                1]  # выводим часть, которую мы разбивали по символу точка,
                    # и в списке по середине будет слово - его и выводим
        else:  # иначе, если нету в адресе комбинации www, то часть после двойного слеша разделяем по точке
                # и выводим часть от двойного слеша и до точки
            a[1] = a[1].split('.')
            return a[1][0]
    else:  # иначе, если в адресе нету двойного слеша, то ...
        if 'www' in url:  # проверяем наличие комбинации www, если она есть, то разделяем адрес по точке
            # и выводим строку от первой точки до второй
            a = url.split('.')
            return a[1]
        else:  # иначе если нету ни двойного слеша, ни комбинации www, то делим по точке и выводим первую часть
            a = url.split('.')
            return a[0]

        # код ниже не стоит удалять, он нужен для проверки


assert get_domain_name("http://google.com") == "google"
assert get_domain_name("http://google.co.jp") == "google"
assert get_domain_name("www.xakep.ru") == "xakep"
assert get_domain_name("https://youtube.com") == "youtube"

assert get_domain_name("http://github.com/carbonfive/raygun") == 'github'
assert get_domain_name("http://www.zombie-bites.com") == 'zombie-bites'
assert get_domain_name("https://www.siemens.com") == 'siemens'
assert get_domain_name("https://www.whatsapp.com") == 'whatsapp'
assert get_domain_name("https://www.mywww.com") == 'mywww'
print('Проверки пройдены')
