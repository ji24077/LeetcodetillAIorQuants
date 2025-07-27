# Write your MySQL query statement below
SELECT 
    p.product_name,      -- 제품 이름
    o.product_id,        -- 제품 ID
    o.order_id,          -- 주문 ID
    o.order_date         -- 주문 날짜
FROM Orders AS o
JOIN Products AS p
    ON o.product_id = p.product_id
JOIN (
    -- \U0001f525 각 product_id 별로 가장 최근 주문일(max_date)을 구하는 서브쿼리
    SELECT product_id, MAX(order_date) AS max_date
    FROM Orders
    GROUP BY product_id
) AS recent
    ON o.product_id = recent.product_id
   AND o.order_date = recent.max_date   -- \U0001f525 최신 날짜와 일치하는 주문만 남김
ORDER BY p.product_name, o.order_id;