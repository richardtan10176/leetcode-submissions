class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        healthyFruit = 0
        infectedFruit = 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        maxTime = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    healthyFruit += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        if healthyFruit == 0:
            return 0
        while q and infectedFruit < healthyFruit:
            l = len(q)
            maxTime += 1
            for _ in range(l):
                cr, cc = q.popleft()
                print(q)
                for dr, dc in dirs:
                    nr, nc = cr + dr, cc + dc
                    
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        print(nr, nc, maxTime)
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        infectedFruit += 1
                        
            
        return maxTime if infectedFruit == healthyFruit else -1
                        
                