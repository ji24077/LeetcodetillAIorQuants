class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      intervals.sort(key= lambda x: x[0])

      result = []
      result.append(intervals[0])
      



      for i in range(1, len(intervals)):
        curr = intervals[i] # [2,6]
        last = result[-1]
        if last[1] >= curr[0]:
          #ie) 3>=2
          last[1] = max(last[1], curr[1])
        else:
          result.append(intervals[i])

      return result

          

