SELECT s.product_id,
       s.year AS first_year,
       s.quantity,
       s.price
FROM Sales AS s
JOIN (
    SELECT product_id, MIN(year) AS first_year #min yr인 테이블과 조인해서 리턴 Inner임.
    FROM Sales
    GROUP BY product_id
) AS m
ON s.product_id = m.product_id AND s.year = m.first_year;