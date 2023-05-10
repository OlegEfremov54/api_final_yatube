**API for YaTube**
Описание
API для проекта **YaTube**(https://github.com/:OlegEfremov54/api_final_yatube.git.
**Автор**
Олег Ефремов
**Как запустить проект**
Скопировать проект с ГИтхаба
```
git clone https://github.com/:OlegEfremov54/api_final_yatube.git
```
```
cd api_yatube
```
Создать окружение и активировать его при работе в Винде:
```
python -m venv venv

Или для работы на Маке :
python3 -m venv venv
Далее везеде для работы на маке использовать python3 вместо python
```
source venv/bin/activate
```
Инсталировать зависимости requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Сделать миграции:
```
python manage.py migrate

Если требуется создать супер Юзера
```
Запустить проект:
```
python manage.py runserver


**Requirements - Требования**
```
Django==2.2.16
django-filter==21.1
djangorestframework==3.12.4
djangorestframework-simplejwt==4.7.2
djoser==2.1.0
Pillow==8.3.1
PyJWT==2.1.0
requests==2.26.0
```

### Technologies Какие технологии используем
- Python 3.9
- Django 2.2.16
- Djangorestframework 3.12.4

## **Примеры запросов API**
```
GET /api/v1/posts/
```
**Пример ответа**
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2023-04-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
---
```
POST /api/v1/posts/
```
**Джейсончик**
```
}
    "text": "string",
    "image": "string",
    "group": 0
}
```
**Response sample**
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2023-04-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
---
```
PUT /api/v1/posts/{id}/
```
**Request sample**
```
{
    "text": "stringstring",
    "image": "string",
    "group": 0
}
```
**Response sample**
```
{
    "id": 0,
    "author": "stringstring",
    "text": "string",
    "pub_date": "2023-04-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
---
```
PATCH /api/v1/posts/{id}/
```
**Request sample**
```
{
    "text": "anotherstring"
}
```
**Response sample**
```
{
    "id": 0,
    "author": "stringstring",
    "text": "anotherstring",
    "pub_date": "2023-04-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
---
```
DELETE /api/v1/posts/{id}/
```
---
```
GET /api/v1/posts/{post_id}/comments/
```
**Response sample**
```
[
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "created": "2023-04-24T14:15:22Z",
        "post": 0
    }
]
```
---
```
POST /api/v1/posts/{post_id}/comments/
```
**Request sample**
```
{
    "text": "string"
}
```
**Response sample**
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2023-04-24T14:15:22Z",
    "post": 0
}
```
---
```
POST /api/v1/jwt/create/
```
**Request sample**
```
{
    "username": "string",
    "password": "string"
}
```
**Response sample**
```
{
    "refresh": "string",
    "access": "string"
}
```
