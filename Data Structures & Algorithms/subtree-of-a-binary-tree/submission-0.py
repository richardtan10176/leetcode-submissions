# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root1, root2) -> bool:
            if not root1 and not root2:
                return True
            if not root1 and root2 or root1 and not root2:
                return False
            if root1.val != root2.val:
                return False
            if not sameTree(root1.left, root2.left):
                return False
            if not sameTree(root1.right, root2.right):
                return False
            return True
        
        def dfs(bruh) -> bool:
            if not bruh:
                return False
            print(bruh.val)
            if sameTree(bruh,subRoot):
                return True
            if dfs(bruh.left) or dfs(bruh.right):
                return True
            return False
               

        return dfs(root)