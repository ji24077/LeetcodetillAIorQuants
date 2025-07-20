# Write your MySQL query statement below
SELECT em.unique_id, e.name
FROM Employees AS e LEFT JOIN EmployeeUNI as em
on e.id = em.id