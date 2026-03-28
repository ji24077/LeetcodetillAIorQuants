class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
      freq_map = {}

      for word in magazine:
        freq_map[word] = freq_map.get(word, 0) + 1

      for word in ransomNote:
        if word not in freq_map or freq_map[word] == 0:
          return False
        freq_map[word] -= 1
      return True