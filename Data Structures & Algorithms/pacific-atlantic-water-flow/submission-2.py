from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        
        def dfs(q):
            visited = set(q)
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                cr, cc = q.popleft()
                for dr, dc in dirs:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[cr][cc] and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return visited
                
        q = deque()
        for row in range(rows):
            q.append((row, 0))
        for col in range(1, cols):
            q.append((0, col))
        pacific = dfs(q)

        q = deque()
        for row in range(rows):
            q.append((row, cols - 1))
        for col in range(cols - 1):
            q.append((rows - 1, col))
        atlantic = dfs(q)
        
        return [list(p) for p in pacific & atlantic]