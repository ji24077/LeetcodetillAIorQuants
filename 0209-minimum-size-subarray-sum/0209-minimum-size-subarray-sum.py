class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
      window_sum = 0
      left = 0
      result = float('inf')
      for right in range(len(nums)):
       window_sum += nums[right] # 2+3+1+2 = 8

       while window_sum >= target:
        result = min(result, right - left + 1)
        window_sum -= nums[left]
        left+=1
      return 0 if result == float('inf') else result

        

      

