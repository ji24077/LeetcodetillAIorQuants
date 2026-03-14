class Solution:
    def isHappy(self, n: int) -> bool:



      seen = set()
      while n != 1 and n not in seen:
        seen.add(n) # get 19
        curr = 0

        while n > 0:
          back = n %10 # get 9

          curr += back*back # 81

          n //= 10 # then now n = 1 -> while n>0-> 1%10 = 1-> 81+ 1= 82

        n = curr
      return n == 1







      # seen = set()


      # while n != 1 and n not in seen:
      #   print(n) # get 19
      #   seen.add(n)
      #   total = 0
      #   while n > 0:
      #     digit = n % 10 # for 19->9
      #     total += digit*digit
      #     n //= 10 # 19->1
      #     #then n>0,-> 1*1 + 81 = 82 

      #   n = total
      # return n == 1
