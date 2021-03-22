class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        if len(envelopes) == 0:
            return 0
        
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums):
            dp = [nums[0][1]]
            for i in range(1, len(nums)):
                if nums[i][1] > dp[-1]:
                    dp.append(nums[i][1])
                else:
                    left = 0
                    right = len(dp) - 1

                    while left < right:
                        mid = left + (right-left) // 2
                        if dp[mid] < nums[i][1]:
                            left += 1
                        else:
                            right = mid
                    dp[left] = nums[i][1]
            return len(dp)
        return lis(envelopes)