"""
В этом задании вам нужно научиться генерировать текст заданной длинны и возвращать его в ответе в виде файла.

- ручка должна получать длину генерируемого текста из get-параметра length;
- дальше вы должны сгенерировать случайный текст заданной длины. Это можно сделать и руками
  и с помощью сторонних библиотек, например, faker или lorem;
- дальше вы должны вернуть этот текст, но не в ответе, а в виде файла;
- если параметр length не указан или слишком большой, верните пустой ответ со статусом 403

Вот пример ручки, которая возвращает csv-файл: https://docs.djangoproject.com/en/4.2/howto/outputting-csv/
С текстовым всё похоже.

Для проверки используйте браузер: когда ручка правильно работает, при попытке зайти на неё, браузер должен
скачивать сгенерированный файл.
"""

from django.http import HttpResponse, HttpRequest
from faker import Faker


def generate_random_text(text_length: int) -> str:
    # Faker не генерирует текст короче 5 символов
    if text_length < 5:
        samples = {1: 'I', 2: 'Ok', 3: 'DRY', 4: 'KISS'}
        return samples[text_length]

    fake = Faker()
    generated_text = fake.text(max_nb_chars=text_length)
    # Добиваем длину томным многоточием...
    if len(generated_text) < text_length:
        generated_text += '.' * (text_length - len(generated_text))
    return generated_text


def generate_file_with_text_view(request: HttpRequest) -> HttpResponse:
    text_length = request.GET.get('length')
    if text_length is None or not text_length.isdigit() or not (0 < int(text_length) < 4097):
        return HttpResponse('Укажите длину текста от 1 до 4096 символов', status=403)

    generated_text = generate_random_text(int(text_length))
    response = HttpResponse(
        content_type="text/plain",
        headers={"Content-Disposition": 'attachment; filename="text.txt"'},
    )
    response.write(generated_text)
    return response
