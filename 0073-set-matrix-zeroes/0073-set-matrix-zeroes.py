class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()

        zero_cols = set()

        num_row = len(matrix)
        num_col = len(matrix[0])

        for r in range(num_row):
          for c in range(num_col):
            if matrix[r][c] == 0:
              zero_rows.add(r)
              zero_cols.add(c)

        for r in range(num_row):
          for c in range(num_col):
            if r in zero_rows or c in zero_cols:
              matrix[r][c] = 0




        