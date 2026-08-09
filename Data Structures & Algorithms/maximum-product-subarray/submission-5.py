# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         n = len(nums)
#         res = -1e9
#         dp = [None] * n
#         def findMaxProduct(i) -> tuple[int, int]: #maximum and minumum for current subarray respo
#             nonlocal res
#             if i == n - 1:
#                 res = max(res, nums[i])
#                 dp[i] = (nums[i], nums[i])
#                 return dp[i]
#             if dp[i]:
#                 return dp[i]
#             max_subarr, min_subarr = findMaxProduct(i + 1)
#             choice_1 = nums[i]
#             choice_2 = nums[i] * max_subarr
#             choice_3 = nums[i] * min_subarr

#             cur_max = max(choice_1, choice_2, choice_3)
#             cur_min = min(choice_1, choice_2, choice_3)

#             dp[i] = (cur_max, cur_min)
#             res = max(res, cur_max)
#             return dp[i]
#         findMaxProduct(0)
#         return res
    
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[n - 1] = (nums[n - 1], nums[n - 1])
        dp1, dp2 = (nums[n - 1], nums[n - 1]), None
        res = nums[n - 1]
        for i in range(n - 2, -1, -1):
            # max_subarr, min_subarr = dp[i + 1]
            max_subarr, min_subarr = dp1
            choice_1 = nums[i]
            choice_2 = nums[i] * max_subarr
            choice_3 = nums[i] * min_subarr
            cur_max = max(choice_1, choice_2, choice_3)
            cur_min = min(choice_1, choice_2, choice_3)

            # dp[i] = (cur_max, cur_min)
            dp2 = (cur_max, cur_min)
            dp1 = dp2
            
            
            res = max(res, cur_max)
        return res
            


        

            
            
            


