from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        @cache
        def dfs(r, c) -> int: # longest increasing path from this point
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            res = 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    res = max(res, 1 + dfs(nr, nc))
            return res
        res = 0
        for row in range(rows):
            for col in range(cols):
                res = max(res, dfs(row, col))
        return res
            
            
