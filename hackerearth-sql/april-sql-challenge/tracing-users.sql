-- https://www.hackerearth.com/problem/sql/tracing-users/
-- Submission successful!

WITH first AS (
    SELECT
        userid,
        MIN(contestdate) AS first_over
    FROM participants
    WHERE ratings >= 1650
    GROUP BY userid
)

SELECT
    userid,
    SUM(
        CASE
            WHEN contestdate < first_over THEN 1
            ELSE 0
        END
    ) + 1
FROM participants
NATURAL JOIN first
GROUP BY userid
ORDER BY userid;
