class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        eucld = []
        for i, n in enumerate(points):
            eucld.append((math.sqrt(( n[0] )**2 + ( n[1] )**2), n))
        
        heapq.heapify_max(eucld)
        print(eucld)
        while len(eucld) > k:
            heapq.heappop_max(eucld)
        res = []
        for x in eucld:
            res.append(x[1])
        return res
