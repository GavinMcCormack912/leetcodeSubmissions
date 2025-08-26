# Last updated: 8/25/2025, 10:06:43 PM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqs = {}
        for i in range(numCourses):
            reqs[i] = []
        
        for req in prerequisites:
            reqs[req[0]].append(req[1])

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if reqs[course] == []:
                return True
            
            visited.add(course)

            for prereq in reqs[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            reqs[course] = []
            return True

        for course in reqs.keys():
            if not dfs(course):
                return False
        return True