-- https://www.hackerearth.com/challenge/competitive/february-sql-challenge/sql/arithmetic-progressions/
-- Submission successful!

WITH progressions AS (
    SELECT
        a,
        (
            SELECT d
            FROM diff
            WHERE d > a
            ORDER BY d ASC
            LIMIT 1
        ) AS d
    FROM first
)

SELECT
    a,
    d,
    a + d * 4 AS term
FROM progressions;
