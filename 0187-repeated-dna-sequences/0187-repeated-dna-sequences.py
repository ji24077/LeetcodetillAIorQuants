class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()         # 논리: 지금까지 본 10글자 substring 저장
        repeated = set()     # 논리: 두 번 이상 등장한 문자열만 저장
        result = []          # 논리: 출력용 정답 리스트

        for i in range(len(s) - 9):  # 논리: 0부터 len(s)-10까지 반복 (10글자 자르기 위해)
            substring = s[i:i+10]    # 논리: 현재 위치에서 길이 10인 substring 추출

            if substring in seen:   # 논리: 이미 본 적 있다면
                repeated.add(substring)  # 논리: 중복되므로 결과 후보에 추가
            else:
                seen.add(substring)      # 논리: 처음 본 거면 seen에 등록

        result = list(repeated)     # 논리: 집합 → 리스트 변환
        return result