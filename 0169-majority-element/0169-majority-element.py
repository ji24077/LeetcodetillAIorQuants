class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        standard = len(nums) // 2

        count = {}

        for num in nums:
          if num not in count:
            count[num] = 0
          count[num] += 1
          if count[num] > standard:
            return num