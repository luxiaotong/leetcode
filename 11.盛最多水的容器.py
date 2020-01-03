#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_water = 0
        while i < j:
            water = (j-i) * min(height[i],height[j])
            if water > max_water:
                max_water = water
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_water
# @lc code=end
