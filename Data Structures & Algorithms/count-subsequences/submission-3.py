from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1 = len(s)
        n2 = len(t)
        @cache
        def dp(i, j) -> int: #the number of distinct subsequences that 
            if j == n2:
                return 1
            if i == n1:
                return 0
            res = dp(i + 1, j)
            if s[i] == t[j]:
                res += dp(i + 1, j + 1)
            
            return res
        return dp(0, 0)

            