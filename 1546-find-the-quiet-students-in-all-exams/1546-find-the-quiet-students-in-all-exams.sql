WITH
-- 1) 각 시험별로 최고·최저 점수 계산
score_bounds AS (
  SELECT
    exam_id,
    MAX(score) AS max_score,
    MIN(score) AS min_score
  FROM Exam
  GROUP BY exam_id
),
-- 2) 한 번이라도 최고/최저 점수 받은 학생 집합
extreme_students AS (
  SELECT DISTINCT e.student_id
  FROM Exam e
  JOIN score_bounds b
    ON e.exam_id = b.exam_id
   AND (e.score = b.max_score OR e.score = b.min_score)
)
-- 3) 최종 결과: 시험에 응시했고, extreme_students에 없는 학생
SELECT DISTINCT
  s.student_id,
  s.student_name
FROM Student s
JOIN Exam e
  ON s.student_id = e.student_id     -- 한 번이라도 시험 본 학생만
WHERE s.student_id NOT IN (
  SELECT student_id FROM extreme_students
)
ORDER BY s.student_id;