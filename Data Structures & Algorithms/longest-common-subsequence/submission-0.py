class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n_i = len(text1)
        n_j = len(text2)

        dp = [[0] * (n_j + 1) for _ in range(n_i + 1)]

        for i in range(n_i - 1, -1, -1):
            for j in range(n_j - 1, -1, -1):
                longest = 0
                if text1[i] == text2[j]:
                    longest += 1 + dp[i + 1][j + 1]
                else:
                    longest += max(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = longest
        return dp[0][0]