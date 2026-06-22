from collections import defaultdict

class Node:
    def __init__(self, x: int = -1, l: 'Node' = None, r: 'Node' = None):
        self.val = int(x)
        self.r = r
        self.l = l
        self.key = -1  # FIX 1: Must store key to evict from dict

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}  # FIX 2: Changed from defaultdict(Node) to avoid auto-insertion

        self.capacity = capacity
        self.curSize = 0
        self.right = Node()
        self.left = Node()
        self.right.l = self.left
        self.left.r = self.right

    def get(self, key: int) -> int:
        if key in self.d:
            # FIX 3: Disconnect node from its current neighbors first
            self.d[key].l.r = self.d[key].r
            self.d[key].r.l = self.d[key].l

            self.d[key].l = self.right.l
            self.d[key].r = self.right
            self.right.l.r = self.d[key]
            self.right.l = self.d[key]
            return self.d[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key].val = value

            # FIX 4: Disconnect node from its current neighbors first
            self.d[key].l.r = self.d[key].r
            self.d[key].r.l = self.d[key].l

            self.d[key].l = self.right.l
            self.d[key].r = self.right
            # FIX 5: Fixed broken pointer chain assignment
            self.right.l.r = self.d[key]
            self.right.l = self.d[key]

        else:
            self.curSize += 1
            if self.curSize > self.capacity: 
                temp = self.left.r
                self.left.r = self.left.r.r
                self.left.r.l = self.left
                # FIX 6: Delete the evicted key from the dictionary
                del self.d[temp.key]
                self.curSize -= 1
            newEntry = Node(value, self.right.l, self.right)
            newEntry.key = key  # FIX 1: Track key
            self.right.l.r = newEntry
            self.right.l = newEntry
            self.d[key] = newEntry