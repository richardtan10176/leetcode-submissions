"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cloned = {}
        q = deque()
        q.append(node)

        
        newHead = Node(node.val)
        cloned[node.val] = newHead
        newTemp = newHead
        while q:
            curNode = q.popleft()
            newTemp = cloned[curNode.val]
            

            for nb in curNode.neighbors:
                if nb.val not in cloned:
                    newNode = Node(nb.val)
                    newTemp.neighbors.append(newNode)
                    cloned[nb.val] = newNode
                    q.append(nb)
                else:
                    newTemp.neighbors.append(cloned[nb.val])
        
        return newHead




        
