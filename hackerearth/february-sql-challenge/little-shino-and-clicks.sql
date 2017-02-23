-- https://www.hackerearth.com/challenge/competitive/february-sql-challenge/sql/little-shino-and-clicks/
-- Submission successful!

SELECT
    sum(numberofclicks) OVER (ROWS UNBOUNDED PRECEDING),
    datecolumn
FROM clicks
ORDER BY datecolumn DESC;
