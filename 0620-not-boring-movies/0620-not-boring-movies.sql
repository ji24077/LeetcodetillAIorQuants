# Write your MySQL query statement below
SELECT *
FROM Cinema
WHERE MOD(id, 2) = 1          -- id가 홀수
  AND description != 'boring' -- boring 영화 제외
ORDER BY rating DESC;         -- rating 내림차순