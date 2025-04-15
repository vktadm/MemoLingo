--Получить новые слова для пользователя
--select *
--from word
--where id not in (
--    select up.word_id
--    from userprogress as up
--    where up.user_id = 2
--)
--limit 10;


--Получить слова по word_id
--select *
--from word
--where id in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10);


--Получить слова со статусом "NotStudy"
--select *
--from word
--where id in (
--    select word_id
--    from userprogress as up
--    where up.user_id = 1 and up.status = 'NotStudy'
--);


