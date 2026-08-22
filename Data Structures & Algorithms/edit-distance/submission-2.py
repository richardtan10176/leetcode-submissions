from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        res = 0
        @cache
        def dp(i, j) -> int: #minimum number of ops needed to make word1[i:] equal to word2[j:]
            #3 choices, we can delete this character, insert the correct one, or change it to the correct one
            if j == n2:
                return n1 - i
            if i == n1:
                return n2 - j
    
            if word1[i] != word2[j]:
                return min(1 + dp(i, j + 1), 1 + dp(i + 1, j), 1 + dp(i + 1, j + 1))
            else:
                return dp(i + 1, j + 1)
        return dp(0, 0)