# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import math

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        l = []
        counter = 0
        while queue:
            length = len(queue)
            l.append([])
            for x in range(length):
                curNode = queue.pop()
                if curNode.left:
                    queue.appendleft(curNode.left)
                if curNode.right:
                    queue.appendleft(curNode.right)
                l[counter].append(curNode.val)
            
            counter += 1
        return l

