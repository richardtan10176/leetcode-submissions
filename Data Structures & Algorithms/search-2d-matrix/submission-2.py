class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        p1, p2 = 0, len(matrix) - 1
        row = matrix[0]
        while p1 <= p2:
            mid = (p1 + p2) // 2
            if matrix[mid][0] == target:
                return True
            elif target > matrix[mid][0] and target <= matrix[mid][-1]:
                row = matrix[mid]
                break
            elif target > matrix[mid][0]:
                p1 = mid + 1
            else:
                p2 = mid - 1
        print(row)

        p1, p2 = 0, len(row) - 1
        while p1 <= p2:
            mid = (p1 + p2) // 2
            if row[mid] == target:
                return True
            elif target > row[mid]:
                p1 = mid + 1
            else:
                p2 = mid - 1

        return False
                