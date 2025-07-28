class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""  # 논리: 가장 긴 회문 substring 저장

        for i in range(len(s)):  # 논리: 각 인덱스를 중심으로 확장 시도
            temp_odd = self.expand(s, i, i)       # 논리: 홀수 길이 회문 (ex. aba)
            temp_even = self.expand(s, i, i + 1)  # 논리: 짝수 길이 회문 (ex. abba)

            # 논리: 지금까지의 result보다 길면 result 갱신
            if len(temp_odd) > len(result):
                result = temp_odd
            if len(temp_even) > len(result):
                result = temp_even

        return result  # 논리: 최종적으로 가장 긴 회문 반환

    def expand(self, s: str, left: int, right: int) -> str:
        # 논리: 좌우가 같을 동안 확장
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 논리: 확장 후의 유효한 회문 구간 반환
        return s[left + 1:right]