class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  
        # 논리: 정렬을 해서 투포인터 방식으로 양쪽에서 탐색 가능
        # 예: [-2,-1,0,1,3]처럼 정렬되면 l/r 이동으로 합 비교가 쉬움

        n = len(nums)   
        result = []     
        # 논리: 결과를 담을 리스트

        for i in range(n):
            # 논리: i를 기준 값으로 삼고 이후 l, r로 조합 탐색
            if i > 0 and nums[i] == nums[i-1]:
                continue
                # 논리: i가 이전 값과 같다면 중복 조합이므로 건너뛴다

            l, r = i+1, n-1  
            # 논리: i 이후의 양 끝에서 투포인터 시작
            while l < r:
                total = nums[i] + nums[l] + nums[r]  
                # 논리: 현재 세 수의 합
                if total == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    # 논리: 합이 0이면 결과에 추가

                    # 논리: 중복 피하기 위해 다음으로 이동
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                      #같은숫자들 은 이미사용해봤으니 중복피하기용.
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif total < 0:
                    l += 1  
                    # 논리: 합이 0보다 작으면 왼쪽 값을 늘려서 합을 키운다
                else:
                    r -= 1  
                    # 논리: 합이 0보다 크면 오른쪽 값을 줄여서 합을 줄인다

        return result