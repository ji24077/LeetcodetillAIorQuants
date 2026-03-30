class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      num_set = set(nums)
      lcs = 0

      for num in num_set:
        if num - 1 not in num_set:
          begin = num

          length = 1
          while num + 1 in num_set:
            num += 1
            length += 1
          lcs = max(length, lcs)
      return lcs


