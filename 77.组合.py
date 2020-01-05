#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def backtrack(self, ans, combo, num, n, k):
        combo.append(num)
        if len(combo) == k:
            ans.append(combo)
            return
        for i in range(num+1, n+1):
            self.backtrack(ans, combo[:], i, n, k)
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        for i in range(1, n+1):
            self.backtrack(ans, [], i, n, k)
        return ans
# @lc code=end

