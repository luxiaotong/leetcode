#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
import sys

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = sys.maxsize
        while True:
            mid = left + (right - left)//2
            #print(left, right, mid, mid**2, (mid+1)**2)
            if x < mid**2:
                right = mid - 1
            elif x < (mid+1)**2:
                return mid
            else:
                left = mid + 1
        
# @lc code=end

s = Solution()
# print("Input: 4, Output: ", s.mySqrt(4))
# print("Input: 8, Output: ", s.mySqrt(8))
# print("Input: 9, Output: ", s.mySqrt(9))
# print("Input: 16, Output: ", s.mySqrt(16))
for i in range(100, 200):
    print("Input: ", i, "Output: ", s.mySqrt(i))