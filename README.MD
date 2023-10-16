# Этот веб-сервис предоставляет REST API.

## 1)Принимает POST-запросы с параметром questions_num для запроса случайных вопросов из внешнего API.

## Сохраняет уникальные вопросы в базе данных PostgreSQL.

### Установка и Запуск

git clone <URL репозитория>

### **Запускаем docker-compose**

docker-compose up -d

### Устанавливаем зависимости

pip install -r requirements.txt

# _Запуск приложения_ 
Создаём таблицу Question в postgresql, с данными указанными в docker-compose 

   
    POSTGRES_DB: postgres
    POSTGRES_USER: postgres
    POSTGRES_PASSWORD: postgres

###### Проверяем подключение через PgAdmin4 

Select *
From questions

###### Так же это приложение можно использовать вместо GET,
###### когда будет использовано @app.route('/api/questions', methods=['POST'])

Чтобы Проверить работает ли функция Заходим в Postman
http://127.0.0.1:5000/api/questions
выбираем метод POST 
    {
        "answer_text": "bones",
        "created_at": "Mon, 16 Oct 2023 09:15:45 GMT",
        "id": 6,
        "question_text": "This material, such as your stapes, is formed by ossification"
    }
