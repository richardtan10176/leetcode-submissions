class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * n
        def dfs(stair) -> int:
            if stair > n:
                return 0
            if stair == n:
                return 1
            if dp[stair] != -1:
                return dp[stair]
            
            total = dfs(stair + 1) + dfs(stair + 2)
            dp[stair] = total
            return total
        
        return dfs(0)
                