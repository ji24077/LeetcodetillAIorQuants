# Write your MySQL query statement below
WITH cte AS (
  SELECT 
    log_id,
    LAG(log_id) OVER(ORDER BY log_id) AS prev_val,  -- 직전 값
    LEAD(log_id) OVER(ORDER BY log_id) AS next_val  -- 다음 값
  FROM Logs
),
start_points AS (
  SELECT log_id, ROW_NUMBER() OVER(ORDER BY log_id) AS rn
  FROM cte
  WHERE prev_val IS NULL OR log_id != prev_val + 1  -- 앞번호와 불연속이면 시작점
),
end_points AS (
  SELECT log_id, ROW_NUMBER() OVER(ORDER BY log_id) AS rn
  FROM cte
  WHERE next_val IS NULL OR log_id != next_val - 1  -- 뒷번호와 불연속이면 끝점
)
SELECT s.log_id AS start_id, e.log_id AS end_id
FROM start_points s
JOIN end_points e
ON s.rn = e.rn;  -- 시작과 끝을 같은 순서로 매칭