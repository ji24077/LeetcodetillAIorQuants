class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        longest = 0

        for num in num_set:
          if num - 1 not in num_set:
            #this is not consecutive, set the start.

            length = 1
            curr = num # begin.
            while curr + 1 in num_set:
              curr +=1
              length +=1
            longest = max(longest, length)
        return longest

