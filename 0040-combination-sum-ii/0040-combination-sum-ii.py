class Solution:#combinationSum2
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 논리: 중복 조합을 쉽게 제거하기 위해 입력 후보를 정렬
      candidates.sort()  # 예: [4,1,2,1] -> [1,1,2,4] 로 정렬

      result = []  # 논리: 모든 유효한 조합을 저장할 리스트
      path = []    # 논리: 현재 탐색 중인 경로(선택된 숫자들)를 임시로 저장

      # 논리: 백트래킹 함수 정의
      def backtrack(start, remain):
          # 논리: remain == 0이면 목표 합을 만족 → 결과에 추가
          if remain == 0:
              result.append(path.copy())  # 현재 path를 복사해 저장
              return

          # 논리: start부터 후보 탐색
          for i in range(start, len(candidates)):
              # 논리: 같은 깊이에서 같은 숫자가 반복되면 중복 조합 발생 → 건너뛰기
              if i > start and candidates[i] == candidates[i-1]:
                  continue

              # 논리: 현재 후보가 remain보다 크면 뒤의 후보도 클 것이므로 탐색 중단
              if candidates[i] > remain:
                  break

              # 논리: 현재 숫자를 path에 추가
              path.append(candidates[i])

              # 논리: 다음 단계로 재귀 호출 (i+1부터, 같은 숫자는 재사용 불가)
              backtrack(i + 1, remain - candidates[i])

              # 논리: 백트래킹 단계 복귀 → 방금 추가한 숫자를 제거
              path.pop()

      # 논리: 초기 호출
      backtrack(0, target)

      return result
          