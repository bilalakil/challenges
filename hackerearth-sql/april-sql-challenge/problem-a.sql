-- https://www.hackerearth.com/problem/sql/problem-a/
-- Submission successful!

SELECT
    item,
    SUM(buyqty) - SUM(sellqty),
    EXTRACT(YEAR FROM trandate) || '/' || EXTRACT(MONTH FROM trandate)
FROM inventory
GROUP BY
    item,
    EXTRACT(YEAR FROM trandate),
    EXTRACT(MONTH FROM trandate)
ORDER BY
    item,
    EXTRACT(YEAR FROM trandate),
    EXTRACT(MONTH FROM trandate);
