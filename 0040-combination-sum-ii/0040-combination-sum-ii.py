class Solution:#combinationSum2
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 논리: candidates는 후보 숫자들의 리스트
        # 논리: target은 우리가 맞추어야 할 합
        candidates.sort()  # 논리: 중복된 숫자들을 인접하게 만들기 위해 정렬, 가지치기에도 유리
        
        result = []  # 논리: 모든 가능한 조합을 저장할 리스트

        def backtrack(start, path, total):
            # 논리: start는 현재 탐색을 시작할 인덱스 (중복 방지)
            # 논리: path는 현재까지 선택한 숫자 조합
            # 논리: total은 현재까지 선택한 숫자들의 합

            if total == target:
                # 논리: 목표 합에 도달하면, path를 결과에 추가
                result.append(list(path))
                return
            if total > target:
                # 논리: 합이 목표를 초과하면 더 탐색할 필요가 없으므로 종료 (pruning)
                return

            prev = None  # 논리: 이전에 선택한 숫자를 기억해서 같은 깊이에서 중복 방지
            for i in range(start, len(candidates)):
                num = candidates[i]  # 논리: 현재 선택할 숫자
                if num == prev:
                    # 논리: 같은 깊이에서 같은 숫자를 중복 선택하지 않기 위해 skip
                    continue
                # 논리: 현재 숫자를 경로에 추가하고 다음 인덱스로 진행
                path.append(num)
                backtrack(i + 1, path, total + num)  # 논리: i+1로 넘겨서 같은 숫자를 두 번 쓰지 않음
                path.pop()  # 논리: 백트래킹 – 선택을 되돌려 다음 후보를 탐색
                prev = num  # 논리: 현재 숫자를 prev로 저장해 다음 루프에서 중복체크
        backtrack(0, [], 0)
        return result