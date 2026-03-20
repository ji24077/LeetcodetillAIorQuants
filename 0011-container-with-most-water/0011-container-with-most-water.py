class Solution:
    def maxArea(self, height: List[int]) -> int:
      left = 0
      right = len(height) - 1
      max_area = 0

      while left < right:
        h = min(height[left], height[right])

        w = right - left
        max_area = max(max_area, h*w)

        if height[left] < height[right]:
          left += 1
        else:
          right -= 1

      return  max_area




















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


      

