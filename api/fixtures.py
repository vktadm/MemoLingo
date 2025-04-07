from core.models import Status

word = [
    {"id": 1, "wrd": "car", "translation": "машина"},
    {"id": 2, "wrd": "house", "translation": "дом"},
    {"id": 3, "wrd": "book", "translation": "книга"},
    {"id": 4, "wrd": "computer", "translation": "компьютер"},
    {"id": 5, "wrd": "tree", "translation": "дерево"},
    {"id": 6, "wrd": "dog", "translation": "собака"},
    {"id": 7, "wrd": "sun", "translation": "солнце"},
    {"id": 8, "wrd": "water", "translation": "вода"},
    {"id": 9, "wrd": "friend", "translation": "друг"},
    {"id": 10, "wrd": "city", "translation": "город"},
]
user = [
    {"id": 1, "username": "admin", "password": "admin"},
    {"id": 2, "username": "user", "password": "user"},
]

user_word = [
    {"user_id": 1, "word_id": 1, "status": "revise"},
    {"user_id": 1, "word_id": 2, "status": "know"},
    {"user_id": 1, "word_id": 3, "status": "revise"},
]
