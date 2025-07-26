# Write your MySQL query statement below
SELECT
  product_id,
  year AS first_year,
  quantity,
  price
FROM Sales
WHERE (product_id, year) IN (
  SELECT product_id, MIN(year) ## 100,200 | 2008,2011이있음.
  FROM Sales
  GROUP BY product_id
);