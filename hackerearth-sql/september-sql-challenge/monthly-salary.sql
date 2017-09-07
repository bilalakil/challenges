-- https://www.hackerearth.com/challenge/competitive/september-sql-challenge/sql/monthly-salary/
-- Submission successful!

SELECT AVG(salary / 12)::INT, MAX(salary / 12)::INT
FROM salaries
WHERE name LIKE 'A%';
