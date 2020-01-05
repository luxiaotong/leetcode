#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0
        ans = 0
        left_max = height[:]
        right_max = height[:]
        for i in range(1, n-1):
            left_max[i] = max(left_max[i-1], height[i])
        for i in range(n-2, 0, -1):
            right_max[i] = max(right_max[i+1], height[i])
        for i in range(1, n-1):
            ans += min(left_max[i], right_max[i]) - height[i]
 
        return ans

# @lc code=end

