# inst-links-dder-bot

Телеграм бот для групповых чатов, который добавляет "dd" в начало ссылок на инст. Это нужно для отображения превью и описания рилсов и постов

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
