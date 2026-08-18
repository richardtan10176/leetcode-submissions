# from functools import cache
# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         n1 = len(s1)
#         n2 = len(s2)
#         n3 = len(s3)
#         @cache
#         def dp(i, j):
#             k = i + j
#             if i == n1 and j == n2:
#                 return True if k == n3 else False
#             if k >= n3: 
#                 return False
            
#             ans = False
#             if i < n1 and s1[i] == s3[k]:
#                 ans = dp(i + 1, j)
#             if not ans and j < n2 and s2[j] == s3[k]:
#                 ans = dp(i, j + 1)
#             return ans
#         return dp(0, 0)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n3 != n1 + n2:
            return False
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[n1][n2] = True
        for i in range(n1, -1, -1):
            for j in range(n2, -1, -1):
                if i == n1 and j == n2:
                    continue
                k = i + j
                ans = False
                if i < n1 and s1[i] == s3[k]:
                    ans = dp[i + 1][j]
                if not ans and j < n2 and s2[j] == s3[k]:
                    ans = dp[i][j + 1]
                dp[i][j] = ans
        return dp[0][0]