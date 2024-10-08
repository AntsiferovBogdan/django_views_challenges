"""
В этом задании вам нужно реализовать ручку, которая принимает на вход ник пользователя на Github,
а возвращает полное имя этого пользователя.

- имя пользователя вы узнаёте из урла
- используя АПИ Гитхаба, получите информацию об этом пользователе (это можно сделать тут: https://api.github.com/users/USERNAME)
- из ответа Гитхаба извлеките имя и верните его в теле ответа: `{"name": "Ilya Lebedev"}`
- если пользователя на Гитхабе нет, верните ответ с пустым телом и статусом 404
- если пользователь на Гитхабе есть, но имя у него не указано, верните None вместо имени
"""

from django.http import HttpResponse, HttpRequest, JsonResponse
import requests


def fetch_name_from_github_view(request: HttpRequest, github_username: str) -> HttpResponse:
    github_api_url = f'https://api.github.com/users/{github_username}'
    try:
        response = requests.get(github_api_url).json()
    except requests.RequestException:
        return HttpResponse('API is unvailable', status=503)
    except requests.JSONDecodeError:
        return HttpResponse('Response is not valid JSON', status=500)

    if response.get('status') == '404':
        return JsonResponse(data={}, status=404)
    return JsonResponse(data={"name": f"{response.get('name')}"}, status=200)
