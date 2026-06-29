# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        LCA = None
        def dfs(root):
            nonlocal LCA
            if not root:
                return
            if p.val < root.val and q.val < root.val: #go left
                dfs(root.left)
            elif p.val > root.val and q.val > root.val: #go right
                dfs(root.right)
            else: #split, so we cant go any lower, so LCA
                LCA = root
                return
            return
        dfs(root)
        return LCA

                


             