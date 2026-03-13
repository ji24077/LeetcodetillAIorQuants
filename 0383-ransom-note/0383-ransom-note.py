class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

      freq = {}

      for char in magazine:
        if char not in freq:
          freq[char] = 0
        freq[char] += 1

      for char in ransomNote:
        if char not in freq:
          return False
        freq[char] -= 1

        if freq[char] < 0:
          return False

      return True



        