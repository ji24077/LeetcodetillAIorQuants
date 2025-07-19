class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []

        intervals.sort(key = lambda x :x[0])

        for interval in intervals:
          start, end = interval

          if not merged or merged[-1][1] < start:
            ## [[1,2],[2,3]]-> merged[-1][1] = 3
            merged.append([start,end])
          else:
            merged[-1][1] = max(merged[-1][1], end)
        return merged



