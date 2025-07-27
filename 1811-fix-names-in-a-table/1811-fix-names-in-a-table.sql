# Write your MySQL query statement below
SELECT
  user_id,
  CONCAT(
    UPPER(LEFT(LOWER(name), 1)),      -- 첫 글자만 대문자로
    LOWER(SUBSTRING(name, 2))         -- 두 번째 글자부터 소문자로
  ) AS name
FROM users
ORDER BY user_id;