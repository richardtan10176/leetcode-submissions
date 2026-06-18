"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = defaultdict(int)
        temp = None
        newHead = None
        while head:
            if id(head) in d:
                newNode = d[id(head)]
            else:
                d[id(head)] = Node(head.val)
                newNode = d[id(head)]
            if temp:
                temp.next = newNode
            else:
                newHead = newNode

            if head.random:
                if id(head.random) not in d:
                    d[id(head.random)] = Node(head.random.val)
                newNode.random = d[id(head.random)]
            

            
            
            temp = newNode
            head = head.next
        return newHead