# Write your MySQL query statement below
SELECT department_name as Department, employee_name as Employee, salary as Salary
FROM (
    SELECT d.name AS department_name,
           e.name AS employee_name,
           e.salary,
           DENSE_RANK() OVER(PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rnk
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
) ranked
WHERE rnk <= 3
ORDER BY department_name ASC, salary DESC;