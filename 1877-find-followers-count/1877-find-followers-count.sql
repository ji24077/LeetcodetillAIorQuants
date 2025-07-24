SELECT DISTINCT f.user_id,
(SELECT COUNT(*) FROM Followers f2 WHERE f2.user_id = f.user_id) AS followers_count
FROM Followers f
ORDER BY f.user_id;