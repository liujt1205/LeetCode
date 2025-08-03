# Write your MySQL query statement below
SELECT query_name, ROUND(AVG(quality), 2) as quality, ROUND(AVG(poor) * 100, 2) as poor_query_percentage FROM
(
    SELECT query_name, position, rating, (rating / position) as quality, (CASE WHEN rating < 3 THEN 1 ELSE 0 END) as poor FROM Queries
) as temp
GROUP BY query_name