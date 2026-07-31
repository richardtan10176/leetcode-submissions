class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        adj = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
        def dfs(root, parent):
            if root in visited:
                return False
            visited.add(root)
            for leaf in adj[root]:
                if leaf == parent:
                    continue
                if not dfs(leaf, root):
                    return False
            return True
            

        visited = set()
        return dfs(0, -1) and len(visited) == n

        
