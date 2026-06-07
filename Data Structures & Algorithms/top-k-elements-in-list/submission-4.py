import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fmap = defaultdict(int)
        for num in nums:
            fmap[num] += 1
        sorted_items = sorted(fmap.items(), key=lambda item: item[1], reverse=True)
        res = []
        for x in range(k):
            res.append(sorted_items[x][0])

        return res
        
