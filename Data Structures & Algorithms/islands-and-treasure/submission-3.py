class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))
                    # visited.add((row, col))
            

        def bfs():
            distance = 1
            while q:
                l = len(q)
                print(l)
                for _ in range(l):
                    cr, cc = q.popleft()
                    for dr, dc in dirs:
                        nr, nc = dr + cr, dc + cc
                        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] > 0:
                            grid[nr][nc] = min(grid[nr][nc], distance)
                            visited.add((nr, nc))
                            q.append((nr, nc))
                distance += 1
                    
        bfs()


        

                    