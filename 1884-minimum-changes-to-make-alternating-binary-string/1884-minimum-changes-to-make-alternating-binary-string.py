class Solution:
    def minOperations(self, s: str) -> int:
        cost_a = 0
        cost_b= 0
        for i, ch in enumerate(s):
          if i % 2 == 0:
            if ch != '0':
              cost_a +=1
            if ch != '1':
              cost_b +=1
          else:
            if ch != '0':
              cost_b +=1
            if ch != '1':
              cost_a +=1
        return min(cost_a, cost_b)