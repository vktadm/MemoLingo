select *
from word
where id not in (
    select up.word_id
    from userprogress as up
    where up.user_id = 2
)
limit 10;

--insert into word (wrd, translation)
--values
--('house', 'дом'),
--('car', 'машина'),
--('tree', 'дерево'),
--('book', 'книга'),
--('pen', 'ручка'),
--('apple', 'яблоко'),
--('table', 'стол'),
--('chair', 'стул'),
--('door', 'дверь'),
--('window', 'окно'),
--('computer', 'компьютер'),
--('phone', 'телефон'),
--('music', 'музыка'),
--('film', 'фильм'),
--('school', 'школа'),
--('university', 'университет'),
--('library', 'библиотека'),
--('park', 'парк'),
--('garden', 'сад');

--insert into userprogress (user_id, word_id, status)
--values
--(1, 1, 'Новое слово'),
--(1, 2, 'Новое слово'),
--(1, 3, 'Новое слово'),
--(1, 4, 'Новое слово'),
--(2, 5, 'Новое слово'),
--(2, 6, 'Новое слово'),
--(2, 7, 'Новое слово'),
--(2, 8, 'Новое слово');