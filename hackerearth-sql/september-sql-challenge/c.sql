-- https://www.hackerearth.com/challenge/competitive/september-sql-challenge/sql/c/
-- Submission successful!

WITH zones AS (
    SELECT
        id,
        STRING_AGG(zone, ',' ORDER BY zone) AS zones
    FROM details
    GROUP BY id
)

SELECT STRING_AGG(name, ',' ORDER BY name)
FROM animals
NATURAL JOIN zones
GROUP BY zones
ORDER BY SUM(strength) DESC
LIMIT 1;
