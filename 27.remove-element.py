#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
from typing import List

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = 0
        len_nums = len(nums)
        i = 0
        while i < len_nums:
            if nums[i] != val:
                length += 1
            else:
                nums[i] = nums[len_nums-1]
                len_nums -= 1
                i -= 1
            i += 1
        #print(nums)
        return length
        
# @lc code=end

s = Solution()
print(s.removeElement([3,2,2,3], 2))
print(s.removeElement([0,1,2,2,3,0,4,2], 2))