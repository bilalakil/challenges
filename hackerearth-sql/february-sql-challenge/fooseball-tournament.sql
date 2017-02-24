-- https://www.hackerearth.com/challenge/competitive/february-sql-challenge/sql/fooseball-tournament/
-- Submission successful!

SELECT
    team_name,
    rank() OVER (ORDER BY count(DISTINCT strength) DESC) AS standing
FROM strength
NATURAL JOIN team
GROUP BY team_name;
