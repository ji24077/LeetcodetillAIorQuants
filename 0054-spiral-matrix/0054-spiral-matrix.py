class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      left = 0
      top = 0
      right = len(matrix[0]) - 1 # 2
      bottom = len(matrix) - 1
      result = []

      while left <= right and top <= bottom:

        for r in range(left, right + 1):
          result.append(matrix[top][r])

        top +=1
        
        for c in range(top, bottom + 1):
          result.append(matrix[c][right])
        right -= 1
        if top <= bottom:
          for r in range(right, left - 1, -1):
            result.append(matrix[bottom][r])
          bottom -= 1
        if left <= right:
          for c in range(bottom, top - 1, - 1):
            result.append(matrix[c][left])
          left += 1
      return result
      


