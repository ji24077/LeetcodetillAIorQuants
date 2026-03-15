class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        left = 0
        sub_len = 0
        for right in range(len(s)):
          
          while s[right] in seen:
            
            seen.remove(s[left])
            left += 1

          seen.add(s[right])
          sub_len = max(sub_len, right - left + 1)
            
        return sub_len

        



