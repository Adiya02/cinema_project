# 🎬 Онлайн-кинотеатр (Django)

Лабораторная работа: тематическое Django-приложение с сохранением
пользовательских настроек (жанр, тема, язык, последние жанры) через cookies.

## Возможности

- Выбор жанра фильмов: Боевики, Комедии, Драмы, Фантастика, Ужасы
- Отображение подборки фильмов по выбранному жанру
- Переключение светлой / тёмной темы
- Выбор языка интерфейса
- История последних выбранных жанров
- Сброс настроек одной кнопкой

## Стек

- Python 3.13
- Django 6.1
- HTML + CSS
- Cookies для хранения настроек

## Установка и запуск

```bash
git clone <ссылка на репозиторий>
cd cinema_project

python -m venv venv
.\venv\Scripts\Activate.ps1     # Windows
source venv/bin/activate         # Linux / macOS

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Открыть в браузере: **http://127.0.0.1:8000/**

## Тесты

```bash
python manage.py test
```

## Структура проекта

```
cinema_project/
├── cinema/              # Приложение кинотеатра
│   ├── data.py          # Данные о жанрах и фильмах
│   ├── urls.py          # URL-маршруты приложения
│   ├── views.py         # Представления
│   └── tests.py         # Тесты
├── config/              # Настройки Django-проекта
├── static/cinema/css/   # Стили
├── templates/cinema/    # HTML-шаблоны
├── manage.py
└── requirements.txt
```