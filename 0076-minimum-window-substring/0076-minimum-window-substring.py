class Solution:
    def minWindow(self, s: str, t: str) -> str:

      need = {}

      for ch in t:
        need[ch] = need.get(ch,0) + 1

      #now we have A:1, B:1..

      window = {}
      result_len = float('inf')
      have = 0
      need_count = len(need)
      result_start = 0
      left = 0



      for right in range(len(s)):
        ch = s[right]
        window[ch] = window.get(ch, 0) + 1

        if ch in need and window[ch] == need[ch]:
          have += 1 # A :1, both, so we have 1 rn
        while have == need_count:
          #if we satisfy the valid window, we have to check is there min subarray
          curr_window_len = right - left + 1

          if curr_window_len < result_len:
            result_len = curr_window_len
            result_start = left #need to store the shortest subarray startindex.

          #now we can remove left_word to check is it possible to find shorter.

          left_char = s[left] #in this case, A
          window[left_char] -= 1 # A: 0 now,
          if left_char in need and window[left_char] < need[left_char]:
            #if its not valid, we minus have, since its not valid have.

            have -= 1
          left += 1 # we do the same thing here.
      if  result_len == float('inf'):
          return ""
      return s[result_start : result_start + result_len]
          


            



        