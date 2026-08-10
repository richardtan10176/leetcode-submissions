class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [None] * n

        def dfs(i):
            
            if i == n:
                return True
            if i > n:
                return False
            if dp[i] is not None:
                return dp[i]
        
            for word in wordDict:
                if s[i:i + len(word)] == word and dfs(i + len(word)):
                    dp[i] = True
                    return True
            dp[i] = False
            return False
        dfs(0)
        return dp[0]
                