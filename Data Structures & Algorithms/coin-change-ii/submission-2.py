from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @cache
        def dfs(i, remainder) -> int:
            if remainder == 0:
                return 1
            if i == n:
                return 0
            combs = 0
            if remainder - coins[i] >= 0:
                combs += dfs(i, remainder - coins[i])
            combs += dfs(i + 1, remainder)
            return combs
        return dfs(0, amount)