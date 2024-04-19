Проект «Доска объявлений»

Данный проект представляет собой платформу для размещения объявлений, которая помогает пользователям найти друг друга. На этой платформе каждый пользователь может размещать объявления о продаже товаров и услуг, а также имеет возможность выбрать для себя товар или услугу необходимого качества на выгодных для себя условиях.

О проекте

Проект состоит из двух основных частей: backend-части на основе Django и frontend-части (написана сторонним пользователем). Backend обеспечивает API для работы с объявлениями.

Возможности проекта

Регистрация и авторизация пользователей.
Распределение ролей между пользователями (пользователь и админ).
Создание, чтение, обновление и удаление объявлений на основании прав доступа.
Создание, чтение, обновление и удаление комментариев под каждым объявлением на основании прав доступа.
Просмотр списка объявлений и их чтение с пагинацией.
Поиск объявлений по названию в заголовке сайта.

Запуск проекта

Склонируйте репозиторий:
github.com
Для запуска проекта необходимо установить docker
docker.com
Установите зависимости:
pip install -r requirements.txt
Создайте файл .env в корневой директории и заполните необходимые переменные окружения:
SECRET_KEY=секретный_ключ

DB_ENGINE=база_данных

DB_NAME=название_базы_данных

DB_USER=пользователь_базы_данных

DB_PASSWORD=пароль_базы_данных

DB_PORT=порт_базы_данных

DB_HOST=хост_базы_данных

Примените миграции:

python skymarket/manage.py migrate
Запустите сервер:
python skymarket/manage.py runserver
Используйте команду csu для создания суперпользователя:
python skymarket/manage.py csu
Документация API
Документация API доступна после запуска сервера по ссылке redoc

Docker

Для создания образа из Dockerfile запустите команду docker-compose build

Для запуска контейнера используйте команду docker-compose up

Для остановки контейнера используйте команду docker-compose down
