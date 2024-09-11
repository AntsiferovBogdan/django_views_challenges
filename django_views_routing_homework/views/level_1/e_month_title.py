from django.http import HttpResponse, HttpResponseNotFound, HttpRequest


"""
Вьюха get_month_title_view возвращает название месяца по его номеру. 
Вся логика работы должна происходить в функции get_month_title_by_number.

Задания:
    1. Напишите логику получения названия месяца по его номеру в функции get_month_title_by_number
    2. Если месяца по номеру нет, то должен возвращаться ответ типа HttpResponseNotFound c любым сообщением об ошибке
    3. Добавьте путь в файле urls.py, чтобы при открытии http://127.0.0.1:8000/month-title/тут номер месяца/ 
       вызывалась вьюха get_month_title_view. Например http://127.0.0.1:8000/month-title/3/ 
"""
from calendar import month_name
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU')


def get_month_title_by_number(month_number: int):
    if type(month_number) is int and 0 < month_number < 13:
        month_title = month_name[month_number].capitalize()
        if month_title.endswith('а'):
            month_title = month_title[:-1]
        else:
            if month_number == 5:
                month_title = month_title[:-1] + 'й'
            else:
                month_title = month_title[:-1] + 'ь'
        return month_title
    return False


def get_month_title_view(request: HttpRequest, month_number: int) -> HttpResponse:
    month_title = get_month_title_by_number(month_number)
    if month_name:
        return HttpResponse(month_title)
    return HttpResponseNotFound('Месяца с таким номером не существует')
