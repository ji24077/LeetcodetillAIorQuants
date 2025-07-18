class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      #ie) [3,2,2,3]->[2,2,2,2]-> but k inc if nums[i]!=val
      #ie) 2 != 3 -> 
      k = 0
      for i in range(len(nums)):
        if nums[i] != val:
          nums[k] = nums[i] #do not need to remove it
          k+=1
      return k
        