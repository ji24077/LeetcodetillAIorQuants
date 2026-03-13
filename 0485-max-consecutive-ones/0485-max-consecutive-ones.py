class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
      result = 0
      left = 0
      for right in range(len(nums)):
        if nums[right] != 1:
          left = right + 1
        

          
        result = max(result, right - left + 1)
      return result

        