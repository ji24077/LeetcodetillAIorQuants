SELECT -- ▶ 전체 급여 중 가장 높은 값을 구한다.
  MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);
-- ▶ 최고 급여보다 작은 값들 중에서
-- ▶ 그 중 가장 큰 값 = 두 번째로 높은 급여