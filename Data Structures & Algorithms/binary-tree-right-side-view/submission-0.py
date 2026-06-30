# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        res = []
        q.append(root)
        while q:
            l = len(q)
            res.append(q[0].val)
            for _ in range(l):
                curNode = q.pop()
                if curNode.left:
                    q.appendleft(curNode.left)
                if curNode.right:
                    q.appendleft(curNode.right)
        return res