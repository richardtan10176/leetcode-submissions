class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]
        
        def dfs(i: int, holding: bool) -> int:
            if i >= n:
                return 0
            
            state = 1 if holding else 0
            if dp[i][state] != -1:
                return dp[i][state]
            
            if holding:
                res = max(dfs(i + 1, True), dfs(i + 2, False) + prices[i])
            else:
                res = max(dfs(i + 1, False), dfs(i + 1, True) - prices[i])
            
            dp[i][state] = res
            return res
        
        return dfs(0, False)