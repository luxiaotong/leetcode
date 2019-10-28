#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        past = None
        
        for i in range(len(nums)):
            if past == None:
                past = nums[i]
                nums[length] = nums[i]
                length += 1
            elif nums[i] == past:
                continue
            else:
                past = nums[i]
                nums[length] = nums[i]
                length += 1
        return length
# @lc code=end

s = Solution()
nums = [1,1,2]
length = s.removeDuplicates(nums)
print(length)
print(nums[:length])
nums = [0,0,1,1,1,2,2,3,3,4]
length = s.removeDuplicates(nums)
print(length)
print(nums[:length])