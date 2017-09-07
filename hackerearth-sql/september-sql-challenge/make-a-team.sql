-- https://www.hackerearth.com/challenge/competitive/september-sql-challenge/sql/make-a-team/
-- They're having technical difficulties,
-- so I couldn't attempt submission before the competition ended :(
-- https://www.hackerearth.com/challenge/competitive/september-sql-challenge/sql/make-a-team/?scroll-id=comments-551-1241&scroll-trigger=inview#c116191
-- Found that it was correct afterwards.

WITH overlap AS (
    SELECT
        *,
        COALESCE(LAG(startempid) OVER (), 0) AS prev_startempid,
        COALESCE(LAG(endempid) OVER (), 0) AS prev_endempid
    FROM teams
), tagged AS (
    SELECT
        endempid - startempid + 1 AS n,
            CASE WHEN prev_endempid >= startempid
                THEN prev_endempid - startempid + 1
                ELSE 0
            END AS o
    FROM overlap
)

SELECT SUM((n * (n + 1)) / 2 - (o * (o + 1)) / 2) FROM tagged;
