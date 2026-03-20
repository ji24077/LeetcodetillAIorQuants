class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
      left = 0
      window_sum = 0
      window_len = float("inf")
      for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum >=target:
          window_sum -= nums[left]
       
          window_len = min(window_len, right - left + 1)
          left += 1

          
      return window_len if window_len != float("inf") else 0


          
        

          
















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
          




          


      

