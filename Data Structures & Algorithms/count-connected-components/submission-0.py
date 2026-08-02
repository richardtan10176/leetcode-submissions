class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = set()
        res = 0

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node):
            for nei in adj[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)
            return


        for node in range(n):
            if node not in visit:
                visit.add(node)
                dfs(node)
                res += 1
        return res
            