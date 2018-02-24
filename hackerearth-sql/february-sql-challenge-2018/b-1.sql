-- https://www.hackerearth.com/problem/sql/b-1/
-- Submission successful!

SELECT person.personID, person.name, COUNT(friend.personId), SUM(friend.score)
FROM Person as person
JOIN Friend as friendRel ON person.personId = friendRel.personId
JOIN Person as friend ON friend.personId = friendRel.friendId
GROUP BY person.personId
HAVING SUM(friend.score) > 100
ORDER BY person.personID ASC;
