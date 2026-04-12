class Solution:
    def maxArea(self, height: List[int]) -> int:
      left = 0
      right = len(height) - 1
      area = 0

      while left <= right:
        w = right - left 
        h = min(height[left], height[right])

        if height[left] < height[right]:
          left += 1
        else:
          right -= 1
        area = max(area, w*h)

      return area
