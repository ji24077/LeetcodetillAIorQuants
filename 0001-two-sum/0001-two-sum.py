class Solution:
    def twoSum(self, nums, target):
       seen = {}

       n = len(nums)

       for i in range(n):
        num = nums[i]

        needed = target - num

        if needed in seen:
          return [seen[needed], i]

        seen[num] = i