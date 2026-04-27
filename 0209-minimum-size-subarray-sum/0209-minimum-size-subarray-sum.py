class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")

        left = 0
        cur_sum = 0
        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= target:
                cur_sum -= nums[left]

                min_len = min(min_len, right - left + 1)

                left += 1
        return min_len if min_len != float("inf") else 0
        






        










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
          




          


      

