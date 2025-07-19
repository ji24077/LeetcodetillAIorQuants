class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        tMaps = {}   # t의 문자 → s의 문자 매핑을 저장할 딕셔너리
        sMapt = {}   # s의 문자 → t의 문자 매핑을 저장할 딕셔너리

        # 두 문자열을 같은 길이만큼 순회하면서 매핑을 검증
        for i in range(len(s)):
            ch_s = s[i]  # s에서 현재 문자
            ch_t = t[i]  # t에서 현재 문자

            # \U0001f50e [s → t 매핑 확인]
            if ch_s in sMapt:                 # s 쪽 문자가 이미 매핑된 적이 있는지 확인
                if sMapt[ch_s] != ch_t:       # 과거 매핑된 값과 지금의 t문자가 다르면 충돌
                    return False              # 잘못된 매핑이므로 False 리턴
            else:
                sMapt[ch_s] = ch_t            # 처음 등장한 문자라면 새로운 매핑 등록

            # \U0001f50e [t → s 매핑 확인]
            if ch_t in tMaps:                 # t 쪽 문자가 이미 매핑된 적이 있는지 확인
                if tMaps[ch_t] != ch_s:       # 과거 매핑된 값과 지금의 s문자가 다르면 충돌
                    return False              # 잘못된 매핑이므로 False 리턴
            else:
                tMaps[ch_t] = ch_s            # 처음 등장한 문자라면 새로운 매핑 등록

        return True  # 끝까지 문제없이 매핑이 일관되면 True