# FlowerShop

Вебсайт интернет магазина по продаже цветов.

## Установка:

### 1. Копируем содержимое проекта себе в рабочую директорию

### 2. Разворачиваем внутри скопированного проекта виртуальное окружение:
```
python -m venv <название виртуального окружения>
```

### 3. Устанавливаем библиотеки:
```
pip install -r requirements.txt
```

### 4. Для хранения переменных окружения создаем файл .env:
```
touch .env
```
Генерируем секретный ключ DJANGO в интерактивном режиме python:
* `python`
* `import django`
* `from django.core.management.utils import get_random_secret_key`
* `print(get_random_secret_key())`
    
Копируем строку в `.env` файл: `DJANGO_KEY='ваш ключ'` 

Так же в проекте используются следующие переменные окружения:  
`DEBUG`.  Вкючение/выключение режима отладки. Значение False - выключение режима отладки. Значение True - включение режима отладки.  
`DB_ENGINE`. Используемый бэкенд базы данных.  
`DB_NAME`. Имя используемой базы данных.  
`ALLOWED_HOSTS`. Список строк, представляющих имена хостов/доменов, которые может обслуживать ваш Django-сайт.  
`TG_BOT_TOKEN`. Токен телеграм бота, который сообщает флористу о поступившей заявки на консультацию.  
`TG_CHAT_ID`. Чат ID флориста которому поступает заявка на консультацию от клиента.  

### 5. Переходим в директорию проекта и выполняем миграции в БД: 
```
python manage.py migrate
```

## Использование:

### 1. Создаем панель администратора:

```
python manage.py createsuperuser
```


### 2. Запускаем сервер:

```
python manage.py runserver
```


### 3. Переходим на http://127.0.0.1:8000/ и видим наш сайт.

## Источники данных

1. Фронтенд получает данные из базы данных SQLite3. Данные вы можете вносить через панель администратора.

## Цели проекта

Код написан в учебных целях — это командный проект в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org/).
