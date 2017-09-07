-- https://www.hackerearth.com/challenge/competitive/september-sql-challenge/sql/sql-problem/
-- Submission successful!

WITH ranked AS (
    SELECT house_number, ROW_NUMBER() OVER() AS r
    FROM houses
    ORDER BY house_number
)

SELECT COUNT(*)
FROM ranked AS a
JOIN ranked AS b
    ON a.house_number != b.house_number
WHERE a.house_number < b.house_number
    AND a.house_number % 2 = 1
    AND b.house_number % 2 = 0
    AND a.r % 2 = 0
    AND b.r % 2 = 1;
