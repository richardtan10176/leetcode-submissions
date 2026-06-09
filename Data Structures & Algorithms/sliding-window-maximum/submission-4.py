from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        p1, p2 = 0, 0
        q = deque()
        res = []
        while p2 < len(nums):
            
            while q and nums[q[-1]] < nums[p2]:
                q.pop()
            q.append(p2)
            
            if p2 >= k - 1:
                res.append(nums[q[0]])
                p1 += 1
                if q[0] < p1:
                    q.popleft()
            p2 += 1

        
        return res

                

                
                