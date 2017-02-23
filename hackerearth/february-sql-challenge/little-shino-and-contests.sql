-- https://www.hackerearth.com/challenge/competitive/february-sql-challenge/sql/little-shino-and-contests/
-- Submission successful!

WITH individually_ranked_submissions AS (
    SELECT
        submission_id,
        contest_id,
        contestant_id,
        score,
        rank() OVER (
            PARTITION BY contestant_id
            ORDER BY score DESC
        ) AS rank
    FROM submissions
)

SELECT
    contestant_id,
    contestant_name,
    contest_name,
    submission_id,
    score
FROM individually_ranked_submissions AS cre
    JOIN contestants ON cre.contestant_id = c_id
    JOIN contests ON cre.contest_id = co_id
WHERE rank = 1
ORDER BY contestant_id;
