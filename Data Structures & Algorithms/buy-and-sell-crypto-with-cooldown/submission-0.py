class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]
        def dfs(i, holding) -> int: #the most profit we can make at this state
            if i >= n - 1:
                if holding:
                    return prices[i]
                else:
                    return 0
            if dp[i][1 if holding else 0] != -1:
                return dp[i][1 if holding else 0]
            maxProfit = None
            if holding:
                maxProfit = max(dfs(i + 1, True), dfs(i + 2, False) + prices[i]) #hold, sell
            else:
                maxProfit = max(dfs(i + 1, False), dfs(i + 1, True) - prices[i]) #not buy, buy
            dp[i][1 if holding else 0] = maxProfit
            return maxProfit
        return dfs(0, False)

            
                
                
            
            
# if holding:
# we can sell, or hold

# if not holding:
# we can buy, or not buy


