from collections import defaultdict, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        queue = deque()
        dct = defaultdict(int)
        for task in tasks:
            dct[task] += 1
        for name, freq in dct.items():
            heapq.heappush_max(heap, [freq, name])
            
        time = 1
        while heap or queue:
            if queue:
                if time - queue[-1][1] > n:
                    heapq.heappush_max(heap, queue.pop()[0])
            if heap: 
                curTask = heapq.heappop_max(heap)
                curTask[0] -= 1
                if curTask[0] > 0:
                    queue.appendleft([curTask, time])
            time += 1
            
        return time - 1