class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False

      freq_map = {}
      for word in s:
        freq_map[word] = freq_map.get(word, 0) + 1

      for word in t:
        
        if word not in freq_map:
          return False
        freq_map[word] -= 1

        if freq_map[word] < 0:
          return False
        
      return True