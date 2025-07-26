SELECT s.user_id, 
       -- Signups 테이블의 user_id를 결과로 보여준다.
       
       ROUND(
         IFNULL( AVG(c.action = 'confirmed'), 0 ),
         2
       ) AS confirmation_rate
       -- AVG(c.action='confirmed'): confirmed 비율을 구함 (true=1, false=0 로 평균)
       -- IFNULL(...,0): 데이터가 하나도 없으면 NULL 대신 0으로
       -- ROUND(...,2): 소수점 둘째 자리까지 반올림
       -- AS confirmation_rate: 결과 컬럼 이름을 confirmation_rate로 표시
       
FROM Signups AS s
-- Signups 테이블을 기본으로 사용하고, s 라는 별칭으로 부르겠다.

LEFT JOIN Confirmations AS c
-- Confirmations 테이블을 왼쪽 조인: 가입한 모든 user_id를 유지하면서
-- Confirmations에 일치하는 데이터가 있으면 가져오고, 없으면 NULL로 채운다.

  ON s.user_id = c.user_id
  -- 조인 조건: Signups의 user_id와 Confirmations의 user_id가 같을 때 묶는다.

GROUP BY s.user_id;
-- user_id별로 묶어서 집계한다. (각 user_id마다 AVG를 계산)