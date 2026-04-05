class Solution:
    def maxArea(self, height: List[int]) -> int:
      left = 0
      right = len(height) - 1
      area = 0

      while left < right:
        h = min(height[left], height[right])
        w = right - left


        if height[left] < height[right]:
          left += 1
        elif height[left] >= height[right]: 
          right -= 1
        area = max(w*h, area)
      return area














      # left = 0
      # right = len(height) - 1
      # area = 0

      # while left < right:
      #   h = min(height[left], height[right])
      #   w = right - left

      #   area = max(h * w, area)

      #   if height[left] < height[right]:
      #     left += 1
      #   elif height[left] >= height[right]:
      #     right -=1
      # return area


      

