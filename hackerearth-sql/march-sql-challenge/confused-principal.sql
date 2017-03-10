-- https://www.hackerearth.com/problem/sql/confused-principal/
-- Submission successful!

WITH student_favourites AS (
    SELECT DISTINCT ON (id)
        id,
        student,
        subject
    FROM first
    ORDER BY id, marks DESC
)

SELECT student
FROM second
    JOIN student_favourites
        ON student_favourites.id = second.id
        AND student_favourites.subject = second.subject
WHERE test = 'Yes'
GROUP BY student_favourites.student
HAVING count(*) >= 2
ORDER BY student;
