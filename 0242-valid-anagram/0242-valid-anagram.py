class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        for ch in s:
          if ch in count:
            count[ch] +=1
          else:
            count[ch] = 1
        for ch in t:
          if ch not in count:
            return False
          count[ch] -=1
          if count[ch] == 0:
            del count[ch]

        return len(count) == 0
            