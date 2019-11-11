#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        rst = 0
        arr = list(s)
        arr.reverse()
        for i in range(len(arr)):
            rst += (ord(arr[i]) - 64) * (26 ** i)
        return rst
# @lc code=end

s = Solution()
print("Input: A, Output: ", s.titleToNumber("A"))
print("Input: Z, Output: ", s.titleToNumber("Z"))
print("Input: AA, Output: ", s.titleToNumber("AA"))
print("Input: AB, Output: ", s.titleToNumber("AB"))
print("Input: BA, Output: ", s.titleToNumber("BA"))
print("Input: ZY, Output: ", s.titleToNumber("ZY"))
print("Input: ZZ, Output: ", s.titleToNumber("ZZ"))
print("Input: AAA, Output: ", s.titleToNumber("AAA"))