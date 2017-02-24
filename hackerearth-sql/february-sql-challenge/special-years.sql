-- https://www.hackerearth.com/challenge/competitive/february-sql-challenge/sql/be-an-hr-manager/
-- Submission successful,
-- but only after being punished for not carefully reading the question.

WITH years AS (
    SELECT
        extract(YEAR FROM joiningdate)::INTEGER AS year,
        COUNT(
            CASE
                WHEN extract(MONTH FROM joiningdate)::INTEGER % 2 = 1
                THEN 1
            END
        ) AS odd_months,
        COUNT(
            CASE
                WHEN extract(DAY FROM joiningdate)::INTEGER % 2 = 0
                THEN 1
            END
        ) AS even_days
    FROM employee
    GROUP BY extract(YEAR FROM joiningdate)
    ORDER BY year
)

SELECT
    year AS special_year,
    even_days AS evendays
FROM years
WHERE
    odd_months = 0;
