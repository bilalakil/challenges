-- https://www.hackerearth.com/problem/sql/little-shino-and-swaps/
-- Submission successful!

SELECT
    studentid,
    (
        CASE
            WHEN students.studentid IS NOT NULL THEN score2
            ELSE score1
        END
    ) AS score1,
    (
        CASE
            WHEN students.studentid IS NOT NULL THEN score1
            ELSE score2
        END
    ) AS score2
FROM marks
LEFT OUTER JOIN students USING (studentid);
