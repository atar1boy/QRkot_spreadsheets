# Проект Кошачий Благотворительный Фонд :smiley_cat:

### API Позволяющий получать информацию о благотворительных проетах и автоматически распределять по ним пожертвования.


## Используемые технолологии:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![sqlalchemy](https://img.shields.io/badge/sqlalchemy-%2300f.svg?style=for-the-badge)
![alembic](https://img.shields.io/badge/alembic-3ECF8E?style=for-the-badge&)
![uvicorn](https://img.shields.io/badge/uvicorn-%23DD0031.svg?style=for-the-badge&)
![pydantic](https://img.shields.io/badge/pydantic-39477F?style=for-the-badge&)

## Автор

### Никита Ковалев

### Контакты: [Телеграм](https://t.me/gl_ready/)

## Оглавление:

- [Как запустить проект](#как-запустить-проект)
- [Запуск сервера](#запуск-сервера)
- [Настройка базы данных](#настройка-базы-данных)
- [Ссылка на документацию](#ссылка-на-документацию)

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:atar1boy/cat_charity_fund.git
```

Далее необходимо создать .env файл внутри директории проекта. Пример файла .env:

```
APP_TITLE=TITLE
APP_DESCRIPTION=DESCRIPTION
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=SECRET
FIRST_SUPERUSER_EMAIL=admin@admin.ru
FIRST_SUPERUSER_PASSWORD=admin
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
## Настройка базы данных

Нужно применить миграции с помощью команды:

```
alembic upgrade head 
```

## Запуск сервера

```
uvicorn app.main:app
```

## Ссылка на документацию

Swagger [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Redoc [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
