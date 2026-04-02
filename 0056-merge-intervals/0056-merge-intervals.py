class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      intervals.sort(key = lambda x:x[0]) # sort based on start
      result = []

      result.append(intervals[0]) #add [1,3] first
      for i in range(1, len(intervals)):
        last = result[-1] # current result's last interval, for first its [1,3]
        curr = intervals[i] # current interval [2,6]

        if last[1] >= curr[0]: #last[1] = 3, curr[0] = 2,
          last[1] = max(last[1], curr[1]) # 즉 겹치면, last의 [1,3]-> [1,6]으로 끝을갱신

        else:
          # if not, we just keep the same interval
          result.append(curr)
      return result

