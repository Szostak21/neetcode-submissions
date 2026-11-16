class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]

        preMap = {i: [] for i in range(numCourses)}
        for crs, prq in prerequisites:
            preMap[crs].append(prq)

        possible = set()
        visiting = set()
        order = []

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
            order.append(crs)
            visiting.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return order
