-- https://www.hackerearth.com/problem/sql/count-the-matches/
-- Submission successful!

SELECT count(*)
FROM umpireinfo
WHERE
    (u1 IN ('Bowden', 'Taufel') AND u2 != 'Buckner') OR
    (u2 IN ('Bowden', 'Taufel') AND u1 != 'Buckner');
