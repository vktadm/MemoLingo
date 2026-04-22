API для изучения английских слов с системой интервального повторения FSRS.
## Технологический стек

- **Backend**: FastAPI, Python
- **База данных**: PostgreSQL
- **Кеширование**: Redis
- **ORM**: SQLAlchemy с asyncpg
- **Миграции**: Alembic
- **Аутентификация**: JWT + OAuth 2.0 Google
- **Контейнеризация**: Docker + Docker Compose
## Функциональные возможности

### Категории слов

- Выбор интересующих категорий пользователем
- Фильтрация слов по выбранным категориям
- Обновление предпочтений в реальном времени
### Система изучения слов

**Неизученные слова:**
- Получение списка слов с переводом
- Система свайпов:
  - Влево: слово знакомо - статус "изучено"
  - Вправо: слово незнакомо - статус "на изучении"

**Изучение слов:**
- Слова со статусом "на изучении"
- Проверка знаний с отслеживанием времени
- Гибкая система свайпов для ручного управления статусами

### Аутентификация
- JWT токены через логин/пароль
- OAuth 2.0 интеграция с Google
- Защищенные эндпоинты с проверкой прав
## Архитектура проекта

```
MemoLingo/
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── alembic.ini
│   ├── src/
│   │   ├── app/
│   │   ├── tests/
│   └── alembic/
├── frontend/
│   ├── Dockerfile
│   └── app/
│       ├── package.json
│       ├── vite.config.js
│       └── src/
├── docker-compose.yml
├── .env.example
└── README.md
```
## Локальное развертывание

1. **Клонирование репозитория**
```bash
git clone https://github.com/yourusername/MemoLingo.git
cd MemoLingo
```

2. **Настройка окружения**
Отредактируйте `backend/.env`
```env
# `backend/.env`
SECRET_KEY=your_secret_key  
  
# PostgreSQL settenings  
DB_NAME=db_name  
DB_USER=db_user  
DB_PASSWORD=db_password  
DB_HOST=0.0.0.0  
DB_PORT=5432  
  
# Redis settings  
REDIS_HOST=0.0.0.0  
# REDIS_HOST=redis  
REDIS_PORT=6379  
REDIS_DB=0

# Google OAuth  
GOOGLE_CLIENT_ID=your_client_id  
GOOGLE_CLIENT_SECRET=your_secret
```

3. **Запуск всех сервисов**
```bash
docker-compose up -d --build
```

4. **Проверка работоспособности**
```bash
docker-compose ps
curl http://localhost:8000/health
```
### Доступ к сервисам

| Сервис      | URL                         | Описание                    |
| ----------- | --------------------------- | --------------------------- |
| Backend API | http://localhost:8000       | FastAPI сервер              |
| Swagger UI  | http://localhost:8000/docs  | Документация API            |
| ReDoc       | http://localhost:8000/redoc | Альтернативная документация |
| Frontend    | http://localhost:5173       | Vite + React приложение     |
| PostgreSQL  | localhost:5432              | База данных                 |
| Redis       | localhost:6379              | Кеш и очереди               |
### Инициализация базы данных

```bash
# Применение миграций
alembic init -t async alembic # инициализация alembic
alembic revision --autogenerate -m "Create api_v1 tables"
alembic upgrade head # перейти к последней миграции
```