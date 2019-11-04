#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import List

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        best_sum = 0
        negative_sum = None
        for x in nums:
            if x < 0:
                if negative_sum == None:
                    negative_sum = x
                else:
                    negative_sum = max(negative_sum, x)
            else:
                negative_sum = 0

            current_sum = max(0, current_sum + x)
            best_sum = max(best_sum, current_sum)
        if negative_sum:
            return negative_sum
        else:
            return best_sum
# @lc code=end

s = Solution()
print('Input: [-2,1,-3,4,-1,2,1,-5,4]')
print('Output: ', s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print('Input: [-1]')
print('Output: ', s.maxSubArray([-1]))
print('Input: [-2,-1]')
print('Output: ', s.maxSubArray([-2,-1]))
print('Input: [-1,0,-2]')
print('Output: ', s.maxSubArray([-1,0,-2]))
