# Write your MySQL query statement below
SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month,
#--데이터 포맷은, 항상 trans_date,에서 yr, mth추출할떄사용.
       country,
       COUNT(*)                   AS trans_count, #--row count
       SUM(state = 'approved')    AS approved_count,# --bool, apporved면1, ow 0
       SUM(amount)                AS trans_total_amount,
       SUM((state = 'approved') * amount) AS approved_total_amount
FROM Transactions
GROUP BY month, country
ORDER BY month; # ASC임자동으로 increasing..
## 먼저 month로 오름차정렬, 이후 country알파벳순.