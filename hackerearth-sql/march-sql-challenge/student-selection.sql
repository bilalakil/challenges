-- https://www.hackerearth.com/problem/sql/student-selection/
-- Submission successful!

SELECT round(avg(a.height + b.height + c.height), 2)
FROM students AS a
    JOIN students AS b ON a.name != b.name
    JOIN students AS c ON b.name != c.name;
