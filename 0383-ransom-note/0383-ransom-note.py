class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

      counts = {}
      for ch in magazine:
        counts[ch] = counts.get(ch, 0) + 1 
        ## get(ch, value) = ch 가없음 value return.
      
      for ch in ransomNote:
        if counts.get(ch, 0) == 0:
          return False
        counts[ch] -=1

      return True


        