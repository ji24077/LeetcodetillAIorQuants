class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_len = 100000000
        for i in range(len(nums)):
          total += nums[i] # [2+3..]

          while total >= target:
            curr_len = i - left + 1

            if curr_len < min_len:
              min_len = curr_len
            total-= nums[left]
            left+=1
        return 0 if min_len ==100000000 else min_len