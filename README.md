**Краткое описание сервиса:**

- Сервис реализует CRUD api для взаимодействия с холдерами и транзакциями


- В качестве субд используется postgresql


- В качестве ORM используется SQLAlchemy в связке с Pydantic для валидации и сериализации входных данных


**БД содержит в себе такие таблицы как:**
1. **accounts** - 
2. **orders** - 
3. **transactions** - 
4. **users** - 


**ENDPOINTS:**

{host} / holder / api / v1 / {resource}
1. **/accounts/** - GET/POST
2. **/accounts/{account_id}/** - PUT/DELETE
3. **/orders/** - GET/POST
4. **/orders/{order_id}/** - PUT/DELETE
5. **/users/** - GET/POST
6. **/users/{user_id}/** - PUT/DELETE
7. **/transactions/** - GET/POST
8. **/transactions/{transaction_id}/** - PUT/DELETE
9. **/send_actualize_message/** - отправляет сообщение __Актуализируйте балансы!__ в телеграмм канал


**Описание .env файла**
__Данные для подключения к БД__
- POSTGRES_HOST=db
- POSTGRES_PORT=5432
- POSTGRES_USER=postgres
- POSTGRES_PASSWORD=123
- POSTGRES_DB=postgres

__Данные для подключения к Redis для Celery__
- CELERY_BROKER=redis://redis:6379/0
- CELERY_BACKEND=redis://redis:6379/0

__Бот и канал__
- HOLDER_BOT_TOKEN=
- HOLDER_CHAT_ID=


**Команды для build image и запуска контейнера:**

<!-- docker build -t holder_service .

docker run --env-file ./.env -d -p 8003:8003 --name holder_service holder_service -->
docker-compose up


