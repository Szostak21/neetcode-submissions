class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        preMap = {i: [] for i in range(numCourses)}
        for crs, prq in prerequisites:
            preMap[crs].append(prq)

        visiting = set()
        possible = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in possible:
                return True
            visiting.add(crs)
            for prq in preMap[crs]:
                if not dfs(prq):
                    return False
            possible.add(crs)
            visiting.remove(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True