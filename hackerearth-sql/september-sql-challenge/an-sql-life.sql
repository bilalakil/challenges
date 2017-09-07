-- https://www.hackerearth.com/challenge/competitive/september-sql-challenge/sql/an-sql-life/
-- Submission successful!

WITH avgs AS (
    SELECT ROUND(AVG(sql_quotient)::DECIMAL, 2) AS avg
    FROM students
    GROUP BY group_id
)

SELECT MAX(avg) FROM avgs;
