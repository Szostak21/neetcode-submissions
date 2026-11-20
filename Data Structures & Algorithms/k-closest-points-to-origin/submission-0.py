import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for i in range(len(points)):
            xi = points[i][0]
            yi = points[i][1]
            dist = math.sqrt(xi**2+yi**2)

            heapq.heappush(maxHeap, (-dist,xi,yi))
            if i >= k:
                heapq.heappop(maxHeap)

        return [[x,y] for _,x,y in maxHeap]