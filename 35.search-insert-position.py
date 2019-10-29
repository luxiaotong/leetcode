#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
from typing import List

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = -1
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                index = i
            else:
                return i
        return len(nums)
# @lc code=end

s = Solution()
print("Input: [1,3,5,6], 5, Output:", s.searchInsert([1,3,5,6], 5))
print("Input: [1,3,5,6], 2, Output:", s.searchInsert([1,3,5,6], 2))
print("Input: [1,3,5,6], 7, Output:", s.searchInsert([1,3,5,6], 7))
print("Input: [1,3,5,6], 0, Output:", s.searchInsert([1,3,5,6], 0))