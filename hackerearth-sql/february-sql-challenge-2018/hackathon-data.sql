-- https://www.hackerearth.com/problem/sql/hackathon-data/
-- Submission successful!

SELECT e.event_id, tags, themes
FROM (
    SELECT event_id, STRING_AGG(theme_title, '#') AS themes
    FROM (
        SELECT *
        FROM event_themes
        ORDER BY event_themes ASC
    ) AS e
    GROUP BY event_id
) AS e
JOIN (
    SELECT event_id, STRING_AGG(tag_title, '#') AS tags
    FROM (
        SELECT event_id, tag_title
        FROM event_tags
        JOIN tag_info ON id = tag_id
        ORDER BY tag_id ASC
    ) AS t
    GROUP BY event_id
) AS t ON e.event_id = t.event_id
ORDER BY event_id ASC;
