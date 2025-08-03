# Write your MySQL query statement below
SELECT e.name FROM Employee as e
INNER JOIN 
(
    SELECT em.managerId, count(*) as peep 
    FROM Employee as em
    GROUP BY em.managerId
    HAVING COUNT(*) >= 5
) as m ON e.id = m.managerId