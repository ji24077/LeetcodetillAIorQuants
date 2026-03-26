class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
      left = 0
      min_len = float("inf")
      curr_sum = 0

      for right in range(len(nums)):
          curr_sum += nums[right]

          while curr_sum >= target:
              min_len = min(min_len, right - left + 1)
              curr_sum -= nums[left]
              left += 1

      return 0 if min_len == float("inf") else min_len

          
        

          
















    #   left = 0
    #   window_sum = 0
    #  # result = []
    #   result = float('inf')
      


    #   for right in range(len(nums)):
    #     window_sum += nums[right]
    #     while window_sum >= target:
          
    #       window_sum -= nums[left]
          
    #       result = min(result, right - left + 1)
    #       left += 1
          
          
    #   return result if result != float('inf') else 0
          




          


      

