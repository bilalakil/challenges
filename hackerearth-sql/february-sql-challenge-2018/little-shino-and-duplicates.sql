-- https://www.hackerearth.com/problem/sql/little-shino-and-duplicates/
-- Submission successful!

-- Thanks: https://stackoverflow.com/a/35041172/1406230
CREATE OR REPLACE FUNCTION numch(text, text) RETURNS integer AS
  $$ 
    SELECT length($2) - length(replace($2, $1, '')) 
  $$ LANGUAGE SQL;

SELECT MAX(UserId) AS UserId, Name
FROM Users
WHERE NUMCH(SUBSTR(Name, 1, 1), Name) != LENGTH(Name)
GROUP BY Name
ORDER BY MAX(UserId);
