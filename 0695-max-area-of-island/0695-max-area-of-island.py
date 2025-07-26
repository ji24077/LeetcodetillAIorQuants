class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #(r,c) = (0,0)= start,.
        # 1,1,0
        # 0,1,0
        # 1,0,1
        #dfs -> result = 3 -> (0,1) : visited, keep the result.
        #dfs - >result = max(area= 1, result) = 3
        # dfs - >result = 3.
        visited = set() #keep track the visited node, + its not ovelap.
        result = 0 # track the max area of island.
        def dfs(r,c):
          if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0])):
            return 0
          #dfs searching based on row, col.
          if grid[r][c] == 0:
            return 0 # since its a sea, dont need to traverse.
          if (r,c) in visited:
            return 0 # if already visited, then no need.
          visited.add((r,c))
          area = 1
          area += dfs(r+1,c)
          area += dfs(r-1, c)
          area += dfs(r,c+1)
          area += dfs(r,c-1) #
          return area
        for r in range(len(grid)):
          for c in range(len(grid[0])):
            if grid[r][c] == 1 and {r,c} not in visited:
              result = max(dfs(r,c), result)
        return result


