SELECT
  p.project_id,
  e.employee_id
FROM Project p
JOIN Employee e
  ON p.employee_id = e.employee_id
JOIN (
  SELECT p.project_id, MAX(e.experience_years) AS max_exp
  FROM Project p
  JOIN Employee e
    ON p.employee_id = e.employee_id
  GROUP BY p.project_id
) t
  ON p.project_id = t.project_id
 AND e.experience_years = t.max_exp;