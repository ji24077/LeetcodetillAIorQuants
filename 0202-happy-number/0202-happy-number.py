class Solution:
    def isHappy(self, n: int) -> bool:
      seen = set()


      while n != 1 and n not in seen:
        seen.add(n)
        total = 0
        while n > 0:
          digit = n % 10 # for 19->9
          total += digit*digit
          n //= 10 # 19->1
          #then n>0,-> 1*1 + 81 = 82

        n = total
      return n == 1
