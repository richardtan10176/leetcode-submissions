class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        res = []
        def dfs(r, c) -> bool:
            q = deque()
            q.append((r, c))
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            visited = set()
            pacific, atlantic = False, False
            while q:
                cr, cc = q.popleft()
                if cr == 0 or cc == 0:
                    pacific = True
                if cr == (rows - 1) or cc == (cols - 1):
                    atlantic = True
                if pacific and atlantic:
                    return True
                for dr, dc in dirs:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] <= heights[cr][cc] and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return False
                
                

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col):
                    res.append([row, col])
        return res
