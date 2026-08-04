class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        def dfs(i) -> int:
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
           
            curTotal = max( dfs(i + 1), dfs(i + 2) + nums[i])
            dp[i] = curTotal
            return curTotal

            
        return dfs(0)