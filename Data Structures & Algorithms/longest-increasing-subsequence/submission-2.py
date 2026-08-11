class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1
        dp = [-1] * n
        def findSS(i):
            nonlocal res
            if i == n:
                return 0
            length = 1
            if dp[i] != -1:
                res = max(res, length)
                return dp[i]
           
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    length = max(length, 1 + findSS(j))
            res = max(res, length)
            dp[i] = length
            return length
        for i in range(n):
            findSS(i)
        return res

            