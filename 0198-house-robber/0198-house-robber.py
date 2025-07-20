class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
          return 0 
        if len(nums) == 1:
          return nums[0]

        ## dp[i] = max money robber can get  if we consider till ith house 

        ## dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        prev2 = nums[0] # for tracking i-2th max money, consider first house

        prev1 = max(nums[0], nums[1]) # consider either first or 2nd house.

        for i in range(2, len(nums)):
          current = max(prev1, prev2 + nums[i])
          prev2 = prev1
          prev1 = current
        return prev1
