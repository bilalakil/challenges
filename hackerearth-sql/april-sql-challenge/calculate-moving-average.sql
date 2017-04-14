-- https://www.hackerearth.com/problem/sql/calculate-moving-average/
-- Submission successful!

WITH averages AS (
    SELECT
        ROW_NUMBER() OVER() AS row_num,
        AVG(val) OVER(ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS avg
    FROM data
    OFFSET 2
)

SELECT a.avg
FROM (
    SELECT row_num, CEIL(avg) AS avg
    FROM averages
    ORDER BY row_num DESC
    OFFSET 1
) AS a
ORDER BY row_num;
