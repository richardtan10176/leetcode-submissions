class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    
                    if (0 <= nr < rows and 
                        0 <= nc < cols and 
                        grid[nr][nc] == "1" and 
                        (nr, nc) not in visited):
                        
                        visited.add((nr, nc))
                        q.append((nr, nc))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    res += 1
        
        return res
                    
