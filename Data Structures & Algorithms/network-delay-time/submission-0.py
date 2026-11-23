from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u,v,t in times:
            edges[u].append((t,v))

        minHeap = [(0,k)]
        visited = set()
        res = 0

        while minHeap:
            time, curr = heapq.heappop(minHeap)
            if curr in visited:
                continue
            for edge in edges[curr]:
                t, v = edge
                heapq.heappush(minHeap, (time + t,v))
            res = max(res,time)
            visited.add(curr)

        return res if len(visited) == n else -1
        

