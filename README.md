# BabyJournalBot Web - сайт и REST API для телеграм бота

BabyJournalBot Web - главный компонент проекта BabyJournalBot, работающий на *Django* и *Django Rest Framework*.

Здесь реализован REST API для работы с [телеграм ботом](https://github.com/katorov/bjb-telegram-bot) (регистрация пользователей, добавление событий и т.д.), 
а также сам сайт с личным кабинетом (панелью управления).

## Перед началом работы

1. Установите [Docker](https://www.docker.com/) на вашу операционную систему.
2. Установите [Docker Compose](https://docs.docker.com/compose)
    - Если на предыдущем шаге вы установили Docker Desktop, то этот шаг можно пропустить, т.к.
      Docker Compose установится автоматически

## Установка

1. Клонируйте репозиторий

```bash
$ git clone git@github.com:katorov/bjb-web.git
$ cd bjb-web
```

2. Переименуйте файл `.env-example` в `.env` и измените следующие значения на свои:

```bash
export DEBUG=True # Режим отладки
export SECRET_KEY='django-insecure-(8723e2j3h8752kd' # Секретный ключ

export DB_NAME='babyjournalbot' # Название базы данных
export DB_USER='admin' # Имя пользователя базы данных
export DB_PASSWORD='80118345qQ' # Пароль пользователя базы данных
```

3. Поднимите докер-контейнеры

```bash
$ docker-compose up
```

Если не хватает прав для выполнения команды, попробуйте `$ sudo docker-compose up`

## REST-api

Для работы с API рекомендуется использовать асинхронную обертку на aiohttp: [https://github.com/katorov/bjb-api](https://github.com/katorov/bjb-api)

Синхронная обертка над API в данный момент находится в разработке.

## Демонстрация

### Главная страница

![](https://user-images.githubusercontent.com/60778520/117723217-cc1f5080-b1ea-11eb-9d52-9049f500e8e8.gif)

### Личный кабинет

![](https://user-images.githubusercontent.com/60778520/117722986-7ba7f300-b1ea-11eb-8d24-305f2e77b552.gif)