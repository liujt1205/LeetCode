# Write your MySQL query statement below
SELECT email
FROM (SELECT email, count(id) as c FROM Person GROUP BY email) AS TEMP
WHERE c > 1