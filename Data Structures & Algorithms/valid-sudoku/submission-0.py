class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            s = set()
            for col in range(9):
                num = board[row][col]
                if num != '.':
                    if num in s:
                        return False
                    else:
                        s.add(num)
        
        for row in range(9):
            s = set()
            for col in range(9):
                num = board[col][row]
                if num != '.':
                    if num in s:
                        return False
                    else:
                        s.add(num)
        
        for i in range(0, 3):
            for j in range(0, 3):
                s = set()
                for row in range(i*3, i*3 + 3):
                    for col in range(j*3, j*3 + 3):
                        num = board[col][row]
                        if num != '.':
                            if num in s:
                                return False
                            else:
                                s.add(num)
        return True
            
