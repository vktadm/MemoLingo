## MemoLingo
Приложение для изучения английских слов.
### Технологии
- FastAPI
- PostgreSQL (SQLite - dev)
- SQLAlchemy
- loggin
***
### Функционал
- Категории слов
  - Пользователь выбирает интересные ему категории слов -> сохраняется в настройках пользователя

- Неизученные слова:
    - Приходит список слов c переводом.
    - Если слово знакомо, можно "свайпнуть" влево и оно улетит в изученные.
    - Если незнакомо, то "свайпаем" вправо и начать изучение.
- Изучение слов:
    - . 
    - Ответил неправильно, сиатус не тменяется.
    - Ответил верно, слово меняет статус + ставится временная метка с изменеием статуса. 
    - **Вне зависимости от правильности ответа** можно "свайпнуть":
      - влево и улетит в изученные.
      - вправо останется в неизученных.
- Аутентификация:
  - JWT через логин или пароль
  - OAuth 2.0 Янедекс / Google
  - Настройки пользователя:
    - Кол-во слов на повторение
- Административная понель (midlewere)
  - Загрузка новых слов c сайта списком по категориям
***
### Проектирование

**БД**
- Word
  - wrd: str (уникальное поле)
  - translation: str
  - связь с User через UserProgress
- UserProgress
  - status: Enum ("Новое слово", "На изучении")
- User
    - username: str (уникальное поле)
    - связь с Word через UserProgress

**API**
- **Блок выбор категории**
  - GET `/category/{user_id}` Получаем все категории пользователя 
  - POST `/category/{user_id}` Сохраняем новые категории пользователя

- **Блок неизученные слова**
  - GET `/learn/words/{user_id}`: Получает 15 слов на изучение. Слова, не привязаны к пользователю.
  - POST `/learn/words/{user_id}` с данными {"user_id": ..., "word_id": ..., "status": ...} по каждому слову отдельно.

- **Блок изучение слов**
  - GET `/revise/words/{user_id}`: Получаем все слова со статусом **неизученное**
  - GET `/random`: Получаем 3 рандомных слова на английском (фронт)
  - GET `/revise/check` с данными {"Перевод слова": ..., "То что выбрали": ...} -> bool 
  - POST `/learn/learn/{user_id}`
- **Аутентификация**
  - 
***
### Добавить функционал

- Изучение в 3 этапа
- Категории слов
- Добавить нотификации в тг
- Настройки пользователя
- Авторизацию ??

