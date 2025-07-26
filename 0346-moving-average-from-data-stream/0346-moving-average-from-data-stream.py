class MovingAverage:

    def __init__(self, size: int):
      self.size = size
      self.windowSum = 0
      self.q = deque()
        

    def next(self, val: int) -> float:
      self.q.append(val)
      self.windowSum += val

      if len(self.q) > self.size:
        removed = self.q.popleft()
        self.windowSum -= removed

      return self.windowSum / len(self.q)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)