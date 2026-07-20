class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visitedMatrix = [[0 for _ in range( len(board[0]))] for _ in range(len(board))]
        dirs = [-1, 1]
        def search(i, j, idx):
            if board[i][j] != word[idx]:
                return False

            if len(word) - 1 == idx:
                return True
            
            visitedMatrix[i][j] = True
            
            for dr in dirs:
                if i + dr >= 0 and i + dr < len(board) and not visitedMatrix[i + dr][j] and search(i + dr, j, idx + 1):
                    return True
            for dr in dirs:
                if j + dr >= 0 and j + dr < len(board[0]) and not visitedMatrix[i][j + dr] and search(i, j + dr, idx + 1):
                    return True
            visitedMatrix[i][j] = False
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if search(r, c, 0):
                    return True
        return False


            
            
