# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(root, curMax):
            if not root:
                return 0
            if root.val >= curMax:
                curMax = root.val
                return 1 + dfs(root.left, curMax) + dfs(root.right, curMax)
            else:
                return dfs(root.left, curMax) + dfs(root.right, curMax)

        
        return dfs(root,root.val)