class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visited = set()
        maxSize = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            size = 1

            while q:
                coord = q.popleft()

                qr, qc = coord[0], coord[1]
                for dr, dc in dirs:
                    nr, nc = qr + dr, qc + dc
                    print(nr, nc)
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        size += 1
            return size

                        
                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxSize = max( maxSize, bfs(r, c))
        
        return maxSize



