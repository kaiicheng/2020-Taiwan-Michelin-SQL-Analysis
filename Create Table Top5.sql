CREATE TABLE top5 AS
SELECT id, comment_count, title, author, content, sentiment
FROM ptt_food
WHERE title LIKE '%頤宮%' or title LIKE '%教父牛排%' or title LIKE '%MUME%' or title LIKE '%RAW%' or title LIKE '%JL Studio%';