#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == "": return 0
        arr = [0 for i in range(len(s))]
        for i in range(1, len(s)):
            if s[i-1] == '(' and s[i] == ')':
                arr[i] = arr[i-2] + 2 if i > 1 else 2
            elif s[i-1] == ')' and s[i] == ')':
                # print("i-1, i", i-1, i)
                # print("arr", arr[i-arr[i-1]-2], arr[i-1])
                if i > 1 and i - arr[i-1] - 1 >= 0 and s[i - arr[i-1] - 1] == '(':
                    arr[i] = arr[i-1] + 2
                    if i - arr[i-1] - 1 > 0:
                        arr[i] += arr[i-arr[i-1]-2]
                else:
                    arr[i] = 0
        # print(arr)
        return max(arr)

        
# @lc code=end
# "(()())"
# ")()())"
