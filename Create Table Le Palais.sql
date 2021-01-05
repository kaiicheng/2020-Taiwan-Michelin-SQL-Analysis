CREATE TABLE le_palais AS
SELECT id, comment_count, title, author, content, sentiment
FROM ptt_foodle_palais
WHERE title LIKE '%頤宮%';