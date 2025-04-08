# inst-links-dder-bot

Телеграм бот для групповых чатов, который добавляет "dd" в начало ссылок на инст. Это нужно для отображения превью и описания рилсов и постов

Крайне рекомендую создать файл окружения .env в таком формате:
```
API_KEY=API_KEY
USERS=user_id_1,user_id_2,user_id_3,user_id_4
```

API_KEY - ключ API бота. Можно получить с помощью [BotFather](https://t.me/BotFather).
user_id_n - id пользователей телеграм в формате int. Нужны для фановых штук. Если не нужно, то можно написать любое число.

Нужно учесть, что должен быть хотябы один user_id. При этом нужно проследить, чтобы в `main.py` не было обращения к индексу USERS больше, чем количество указано user_id

Сборка контейнера:
```shell
docker build -t ddodik:latest .
```

Запуск контейнера:
```shell
docker run -d --env-file ./.env --name ddodik ddodik:latest
```

Удаление контейнера с остановкой:
```shell
docker rm -f ddodik
```

Удаление образа:
```shell
docker rmi ddodik:latest
```

Сохранение образа в архив:
```shell
docker save ddodik > ddodik.tar
```

Загрузка образа (или образов) из архива:
```shell
docker load -i ddodik.tar
```
