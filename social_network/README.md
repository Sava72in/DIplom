# Social Network Backend

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com:Sava72in/DIplom.git
    ```

2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

3. Настройте базу данных PostgreSQL в `settings.py`.

4. Выполните миграции:
    ```bash
    python manage.py migrate
    ```

5. Создайте суперпользователя:
    ```bash
    python manage.py createsuperuser
    ```

6. Запустите сервер:
    ```bash
    python manage.py runserver
    ```

## API

- Получение публикаций: `/api/posts/`
- Добавление комментариев к публикации: `/api/posts/{post_id}/comments/`
- Добавление/удаление лайков к публикации: `/api/posts/{post_id}/like/`
