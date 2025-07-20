SELECT
    v.customer_id,                -- 고객 ID
    COUNT(v.visit_id) AS count_no_trans    -- 거래 없는 방문 횟수
FROM Visits AS v LEFT JOIN Transactions AS t
    ON v.visit_id = t.visit_id    -- 방문과 거래를 매칭
WHERE t.transaction_id IS NULL    -- 매칭된 거래가 없을 때만
GROUP BY v.customer_id;           -- 고객별로 집계