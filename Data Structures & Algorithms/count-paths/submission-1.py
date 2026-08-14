from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache
        def move(i, j) -> int:
            if i == m or j == n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            return move(i + 1, j) + move(i, j + 1)
        return move(0, 0)


