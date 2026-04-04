class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
      if not nums:
        return []

      start = nums[0] # 0
      result = []

      for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] != 1:
          if start == nums[i - 1]: #ie) [0,2,4]-> [0,2,4]
          #if its not consecutive, ie) 4-2 = 2 != 1, 
            result.append(str(start)) # append 7 will not happen, 
          #its because we can not add start since it might cont
          else:
            result.append(f"{start}->{nums[i-1]}")
          #0->2, 4->5
          start = nums[i] # start = 4
      # if start != nums[-1]:
      #   #since last index cannot be reach by index
      if start == nums[-1]:
        result.append(str(start))       # 혼자면 "7"
      else:
        result.append(f"{start}->{nums[-1]}")  # 연속이면 "7->9"
      return result







      