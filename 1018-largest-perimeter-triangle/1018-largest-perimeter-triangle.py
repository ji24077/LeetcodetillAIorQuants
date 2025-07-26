class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        ##[2,1,2]-> /-\ where /,\ = 2, - = 1
        nums.sort()
        n = len(nums)

        for i in range(n-1,1,-1):
          a,b,c = nums[i-2], nums[i-1], nums[i]
          ## c is biggest since i is from last index

          if a+b > c:
            return a+b+c
        return 0

