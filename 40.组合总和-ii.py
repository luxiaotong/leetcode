#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def backtrack(self, ans, combo, candidates, pos, target):
        num = sum(combo) + candidates[pos]
        if num == target:
            combo.append(candidates[pos])
            if combo not in ans:
                ans.append(combo)
        elif num < target:
            combo.append(candidates[pos])
            for i in range(pos+1, len(candidates)):
                self.backtrack(ans, combo[:], candidates, i, target)
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans = []
        for i in range(len(candidates)):
            self.backtrack(ans, [], candidates, i, target)
        return ans
# @lc code=end

