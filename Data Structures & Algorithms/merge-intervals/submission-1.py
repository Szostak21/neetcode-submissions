class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []

        for start,end in intervals:
            if not res:
                res.append([start,end])
                continue
            
            if start <= res[-1][1] and end > res[-1][1]:
                res[-1][1] = end

            if start > res[-1][1]:
                res.append([start,end])

        return res

