class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
       
        result = []

        if not nums:
            return result

        start = nums[0]

        for i in range(1, len(nums)):
            # 끊기는 순간에만 구간 확정
            if nums[i] - nums[i-1] != 1: # later index i, and before index i-1
                if nums[i-1] != start:
                  result.append(f"{start}->{nums[i-1]}")
                else:
                  result.append(str(nums[i - 1]))
                start = nums[i]


        # 마지막 구간 처리
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")

        return result