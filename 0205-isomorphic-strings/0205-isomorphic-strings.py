class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMapt = {}  # s → t 매핑
        tMaps = {}  # t → s 매핑

        for sc, tc in zip(s, t):  # zip으로 s,t 동시 순회 (range(len) 불필요)

            # 둘 다 처음 보는 문자 → 매핑 등록
            if sc not in sMapt and tc not in tMaps:
                sMapt[sc] = tc
                tMaps[tc] = sc

            # 기존 매핑과 다르면 False
            elif sMapt.get(sc) != tc or tMaps.get(tc) != sc:
                return False

        return True