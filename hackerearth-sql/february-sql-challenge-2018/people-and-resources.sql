-- https://www.hackerearth.com/problem/sql/people-and-resources/
-- Submission successful!

SELECT
    name,
    address,
    COUNT(1),
    (SELECT floor AS c FROM entries AS in_e WHERE name = e.name GROUP BY floor ORDER BY COUNT(1) DESC LIMIT 1),
    STRING_AGG(DISTINCT resources, ',')
FROM entries AS e
GROUP BY name, address
ORDER BY name ASC;
