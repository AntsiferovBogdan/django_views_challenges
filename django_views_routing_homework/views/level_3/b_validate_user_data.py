"""
В этом задании вам нужно реализовать вьюху, которая валидирует данные о пользователе.

- получите json из тела запроса
- проверьте, что данные удовлетворяют нужным требованиям
- если удовлетворяют, то верните ответ со статусом 200 и телом `{"is_valid": true}`
- если нет, то верните ответ со статусом 200 и телом `{"is_valid": false}`
- если в теле запроса невалидный json, вернуть bad request

Условия, которым должны удовлетворять данные:
- есть поле full_name, в нём хранится строка от 5 до 256 символов
- есть поле email, в нём хранится строка, похожая на емейл
- есть поле registered_from, в нём одно из двух значений: website или mobile_app
- поле age необязательное: может быть, а может не быть. Если есть, то в нём хранится целое число
- других полей нет

Для тестирования рекомендую использовать Postman.
Когда будете писать код, не забывайте о читаемости, поддерживаемости и модульности.
"""
import json
import re

from django.http import HttpResponse, HttpResponseBadRequest, HttpRequest, JsonResponse


def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[a-zA-Z]{2,6}", email)


def validate_user_data_view(request: HttpRequest) -> HttpResponse:
    try:
        user_data = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON format')

    match user_data:
        case {'full_name': full_name, 'email': email, 'registered_from': registered_from}:
            if (
                5 <= len(full_name) < 256
                and is_valid_email(email)
                and registered_from in ['website', 'mobile_app']
            ):
                user_data.setdefault('age', 0)
                if type(user_data['age']) is int and len(user_data) == 4:
                    return JsonResponse(data={"is_valid": "true"}, status=200)
            return JsonResponse(data={"is_valid": "false"}, status=200)
        case _:
            return JsonResponse(data={"is_valid": "false"}, status=200)
