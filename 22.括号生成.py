#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def backtrack(self, ans, s, left, right, N):
        if len(s) == 2*N:
            ans.append(s)
        if left < N:
            self.backtrack(ans, s+'(', left+1, right, N)
        if right < left:
            self.backtrack(ans, s+')', left, right+1, N)

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.backtrack(ans, '', 0, 0, n)
        return ans

        
# @lc code=end

