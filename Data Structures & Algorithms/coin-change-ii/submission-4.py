class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        dp[n][0] = 1

        for i in range(n - 1, -1, -1):
            for remainder in range(amount + 1):
                if remainder - coins[i] >= 0:
                    dp[i][remainder] += dp[i][remainder - coins[i]]
                dp[i][remainder] += dp[i + 1][remainder]
                
        return dp[0][amount]

# 0 <= i <= n  ->
# 0 <= remainder <= amount <-
#         def dfs(i, remainder) -> int:
#             if i == n:
#                 return 1 if remainder == 0 else 0
#             combs = 0
#             if remainder - coins[i] >= 0:
#                 combs += dfs(i, remainder - coins[i])
#             combs += dfs(i + 1, remainder)
#             return combs
#         return dfs(0, amount)



        