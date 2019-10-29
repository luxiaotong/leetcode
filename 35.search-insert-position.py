#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
from typing import List

# @lc code=start
class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     index = -1
    #     for i in range(len(nums)):
    #         if nums[i] == target:
    #             return i
    #         elif nums[i] < target:
    #             index = i
    #         else:
    #             return i
    #     return len(nums)
    
    #binary-search
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start + end)//2
            
            print(start, end , mid)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid+1
            else:
                end = mid-1

        if nums[mid] > target:
            return mid
        else:
            return mid+1
# @lc code=end

s = Solution()
print("Input: [1,3,5,6], 5, \nOutput:", s.searchInsert([1,3,5,6], 5))
print("Input: [1,3,5,6], 2, \nOutput:", s.searchInsert([1,3,5,6], 2))
print("Input: [1,3,5,6], 7, \nOutput:", s.searchInsert([1,3,5,6], 7))
print("Input: [1,3,5,6], 0, \nOutput:", s.searchInsert([1,3,5,6], 0))