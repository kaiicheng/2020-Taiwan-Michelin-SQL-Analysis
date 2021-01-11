CREATE TABLE top10 AS
SELECT id, comment_count, title, author, content, sentiment
FROM ptt_food
WHERE title LIKE '%頤宮%' or title LIKE '%教父牛排%' or title LIKE '%MUME%' or title LIKE '%RAW%' or title LIKE '%JL Studio%' or title LIKE '%A Cut%' or title LIKE '%祥雲龍吟%' or title LIKE '%大三元%' or title LIKE '%請客樓%' or title LIKE '%謙安和%';