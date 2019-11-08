#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # Recursion
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)

        # Recursion
        # ways = 0
        # stairs = [n]
        # while len(stairs) > 0:
        #     x = stairs.pop()
        #     if x == 1:
        #         ways = ways + 1
        #     elif x == 2:
        #         ways = ways + 2
        #     else:
        #         stairs.append(x-1)
        #         stairs.append(x-2)
        # return ways

        # Bottom-Up
        a = 1
        b = 1
        for _ in range(1, n):
            a, b = b, a+b
        return b


# @lc code=end

s = Solution()
print("Input: 1, Output: ", s.climbStairs(1))
print("Input: 2, Output: ", s.climbStairs(2))
print("Input: 3, Output: ", s.climbStairs(3))
print("Input: 4, Output: ", s.climbStairs(4))
print("Input: 35, Output: ", s.climbStairs(35))
print("Input: 38, Output: ", s.climbStairs(38))