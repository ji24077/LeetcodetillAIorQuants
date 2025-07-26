SELECT DISTINCT num AS ConsecutiveNums   -- \U0001f539 중복 제거한 num 값을 ConsecutiveNums 컬럼 이름으로 출력
FROM (
  SELECT
    num,                                           -- \U0001f539 현재 행의 값
    LAG(num, 1) OVER (ORDER BY id) AS prev1,       -- \U0001f539 바로 이전 행의 num
    LAG(num, 2) OVER (ORDER BY id) AS prev2        -- \U0001f539 두 번째 이전 행의 num
  FROM Logs
) AS sub
WHERE num = prev1 AND num = prev2;                 -- \U0001f539 현재 값이 직전 2개의 값과 모두 같을 때만 선택