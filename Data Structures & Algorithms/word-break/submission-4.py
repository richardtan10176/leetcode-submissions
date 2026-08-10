# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         n = len(s)
#         dp = [None] * n
#         def dfs(i):    
#             if i == n:
#                 return True
#             if dp[i] is not None:
#                 return dp[i]
        
#             for word in wordDict:
#                 if s[i:i + len(word)] == word and dfs(i + len(word)):
#                     dp[i] = True
#                     return True
#             dp[i] = False
#             return False
#         dfs(0)
#         return dp[0]
    


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                w_len = len(word)
                if i + w_len <= n and s[i:i + w_len] == word and dp[i + w_len]:
                    dp[i] = True
                    break
        return dp[0]