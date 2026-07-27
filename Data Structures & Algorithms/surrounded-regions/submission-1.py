class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def bfs(q):
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            visited = set()
            while q:
                cr, cc = q.popleft()
                notSurrounded.add((cr, cc))
                for dr, dc in dirs:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O' and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
        rows = len(board)
        cols = len(board[0])
        notSurrounded = set()
        q = deque()
        for row in range(rows):
            if board[row][0] == 'O':
                notSurrounded.add((row, 0))
                q.append((row, 0))
        for col in range(1, cols, 1):
            if board[rows - 1][col] == 'O':
                notSurrounded.add((rows - 1, col))
                q.append((rows - 1, col))
        for col in range(1, cols, 1):
            if board[0][col] == 'O':
                notSurrounded.add((0, col))
                q.append((0, col))
        for row in range(1, rows - 1, 1):
            if board[row][cols - 1] == 'O':
                notSurrounded.add((row, cols - 1))
                q.append((row, cols - 1))
        bfs(q)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O' and (row, col) not in notSurrounded:
                    board[row][col] = 'X'

        