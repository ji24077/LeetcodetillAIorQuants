class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      #idea : [0,0,0,1,1]-> [0,0,1,1,-]
      # [0,0]
      k = 0
      for i in range(len(nums)):
        if k < 2 or nums[i] != nums[k - 2]:
          nums[k] = nums[i]
          k+=1
      return k


        