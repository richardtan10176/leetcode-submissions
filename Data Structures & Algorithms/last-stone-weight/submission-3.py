class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        newStones = []
        heapq.heapify(newStones)
        for num in stones:
            heapq.heappush(newStones, -num)
        
        while len(newStones) > 1:
            print(newStones)
            stone1 = -heapq.heappop(newStones)
            stone2 = -heapq.heappop(newStones)
            

            
            if stone1 != stone2:
                heapq.heappush(newStones, -abs(stone1 - stone2))
        return -newStones[0] if newStones else 0