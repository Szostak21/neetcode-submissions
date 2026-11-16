class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i : [] for i in range(n)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for ngh in adj[node]:
                if not dfs(ngh, node) and ngh != parent:
                    return False
            return True

        noCycles = dfs(0,-1)

        return noCycles and len(visited) == n