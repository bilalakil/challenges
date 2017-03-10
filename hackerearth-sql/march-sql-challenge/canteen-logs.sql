-- https://www.hackerearth.com/problem/sql/canteen-logs/
-- Submission successful!

WITH totals AS (
    SELECT p1, p2, sum(amount) AS amount
    FROM logs
    GROUP BY p1, p2
)

SELECT
    a.p1, a.p2, a.amount - b.amount
FROM totals AS a
    JOIN totals AS b
        ON a.p1 = b.p2
        AND a.p2 = b.p1
WHERE a.amount > b.amount
ORDER BY p1, p2;
