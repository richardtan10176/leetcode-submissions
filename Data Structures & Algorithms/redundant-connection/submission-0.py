class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(edges) + 1)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = set()
        cycle = []
        cycleNode = None

        def dfs(node, parent):
            nonlocal cycleNode
            if node in visited:
                cycleNode = node
                cycle.append(node)
                return True
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    if cycleNode != -1:
                        cycle.append(node)
                    if node == cycleNode:
                        cycleNode = -1
                    
                    return True
        dfs(1, -1)                
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        return []

