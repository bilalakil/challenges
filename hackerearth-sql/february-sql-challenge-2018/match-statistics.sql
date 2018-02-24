-- https://www.hackerearth.com/problem/sql/match-statistics/
-- Submission successful!

SELECT name, -1 * SUM(batting_status - 1)
FROM match_data
GROUP BY name
ORDER BY name ASC;
