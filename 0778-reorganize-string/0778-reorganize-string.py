import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # 논리: 각 문자 빈도 세기 (Counter 안 쓰고 직접)
        freq_map = {}  # 문자 -> 빈도
        for ch in s:               # 문자열 한 글자씩 순회
            if ch in freq_map:     # 이미 있으면 +1
                freq_map[ch] += 1
            else:                  # 없으면 1로 초기화
                freq_map[ch] = 1

        # 논리: 최대 힙 구성 (heapq는 최소힙이므로 음수로 저장)
        max_freq = max(freq_map.values())
        if max_freq > (len(s) + 1) // 2: 
            return ""  # 절대 재배치 불가 ##GPT가 못품!
        max_heap = []
        for ch in freq_map:
            heapq.heappush(max_heap, (-freq_map[ch], ch))
            # 음수 빈도: heapq가 최소힙이라 최대값 뽑기 위해 음수 사용

        result = []  # 최종 문자열을 담을 리스트
        prev_freq = 0  # 직전에 사용한 문자의 남은 빈도
        prev_ch = ""   # 직전에 사용한 문자

        # 논리: 힙에서 하나씩 꺼내며 재배치
        while max_heap:
            freq, ch = heapq.heappop(max_heap)  # 가장 빈도 높은 문자 꺼냄
            result.append(ch)                   # 결과에 추가

            # 논리: 직전에 사용한 문자가 남아있다면 다시 힙에 넣기
            if prev_freq < 0:                   # 남은 빈도 있으면
                heapq.heappush(max_heap, (prev_freq, prev_ch))

            # 논리: 현재 문자 사용 후 빈도 감소
            freq += 1         # 음수이므로 +1 하면 빈도 감소
            prev_freq = freq  # 이번에 사용한 문자를 다음에 기억
            prev_ch = ch

        ans = ''.join(result)  # 리스트를 문자열로 합침

        # 논리: 검증 - 인접한 문자가 같으면 실패
        for i in range(1, len(ans)):
            if ans[i] == ans[i-1]:
                return ""
        return ans