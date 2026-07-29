class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = [[] for _ in range(numCourses)]
        visited = set()
        visiting = set()
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        def dfs(course):  
            if course in visited:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)

            visited.add(course)
            res.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res