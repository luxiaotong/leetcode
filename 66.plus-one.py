#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
from typing import List

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = []
        s = ''.join(str(x) for x in digits)
        n = int(s) + 1
        for x in str(n):
            x = int(x)
            nums.append(x)
        
        return nums

        #return digits
# @lc code=end

s = Solution()
print("Input: [1,2,3], Output: ", s.plusOne([1,2,3]))
print("Input: [4,3,2,1], Output: ", s.plusOne([4,3,2,1]))
print("Input: [0], Output: ", s.plusOne([0]))
print("Input: [9], Output: ", s.plusOne([9]))
print("Input: [1999], Output: ", s.plusOne([1999]))