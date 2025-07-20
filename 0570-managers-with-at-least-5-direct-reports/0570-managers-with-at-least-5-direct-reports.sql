SELECT  e1.name
FROM Employee AS e1
JOIN Employee AS e2
  ON e1.id = e2.managerId       -- e1이 매니저, e2가 그 매니저의 부하직원
GROUP BY e1.id, e1.name
HAVING COUNT(e2.id) >= 5;       -- 부하직원이 5명 이상인 경우만