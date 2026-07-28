class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        arr = [[] for _ in range(numCourses)]
        for c, r in prerequisites:
            arr[c].append(r)
        
        def dfs(course):
            if not arr[course]:
                return True
            if course in visited:
                return False
            visited.add(course)
            for c in arr[course]:
                if not dfs(c):
                    return False
            visited.remove(course)
            arr[course] = []
            return True
        visited = set()
    
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            