WITH all_dates AS(
    -- 1) UserVisits 테이블의 날짜를 그대로 가져오고
    SELECT user_id, visit_date
    FROM UserVisits
    UNION
    -- 2) 각 유저마다 '2021-01-01'이라는 가상 방문일을 추가
    SELECT user_id, '2021-01-01' AS visit_date
    FROM UserVisits
),
rnk AS(
    SELECT *,
        -- 3) 각 user_id별로 날짜를 오름차순 정렬하고 순서를 매김
        RANK() OVER(PARTITION BY user_id ORDER BY visit_date) AS date_rnk
    FROM all_dates
)
-- 4) rnk 테이블을 자기 자신과 조인하여 인접한 날짜 간격을 구함
SELECT a.user_id,
       MAX(DATEDIFF(b.visit_date, a.visit_date)) AS biggest_window
FROM rnk a
JOIN rnk b
  ON a.user_id = b.user_id
 AND b.date_rnk = a.date_rnk + 1   -- b는 a의 바로 다음 날짜
GROUP BY a.user_id;