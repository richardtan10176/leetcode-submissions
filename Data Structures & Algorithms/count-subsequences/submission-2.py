from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1 = len(s)
        n2 = len(t)
        @cache
        def dp(i, j) -> int: #the number of distinct subsequences that 
            if i == n1 or j == n2:
                return 0            
            res = 0
            if j == n2 - 1 and s[i] == t[j]:
                res += 1
            if s[i] == t[j]:
                res += dp(i + 1, j + 1)
            res += dp(i + 1, j)
            return res
        return dp(0, 0)

            