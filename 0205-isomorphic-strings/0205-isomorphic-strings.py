class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMapt = {}
        tMaps = {}
        ##  s->t = e:a, g->d...

        for i in range(len(s)):
          ch_s = s[i]

          ch_t = t[i]

          if ch_s in sMapt:
            if sMapt[ch_s] != ch_t:
              return False

          else:
            sMapt[ch_s] = ch_t

          if ch_t in tMaps:
            if tMaps[ch_t] != ch_s:
              return False
          else:
            tMaps[ch_t] = ch_s
        return True

