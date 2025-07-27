# Write your MySQL query statement below
WITH dept_max AS (
  -- 1) 부서별 최대 연봉 계산
  SELECT
    departmentId,
    MAX(salary) AS max_salary
  FROM Employee
  GROUP BY departmentId
)
-- 2) 최대 연봉자 조회
SELECT
  d.name      AS Department,
  e.name      AS Employee,
  e.salary    AS Salary
FROM Employee e
JOIN dept_max dm ON e.departmentId = dm.departmentId 
AND e.salary = dm.max_salary   -- 부서별 최대 연봉과 일치
JOIN Department d ON d.id = e.departmentId;           -- 부서 이름 붙이기