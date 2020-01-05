#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def backtrack(self, ans, combo, candidates, pos, target):
        num = sum(combo)+candidates[pos]

        if num == target:
            combo.append(candidates[pos])
            ans.append(combo)
            return
        elif num < target:
            combo.append(candidates[pos])
            for i in range(pos, len(candidates)):
                self.backtrack(ans, combo[:], candidates, i, target)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans = []
        for i in range(len(candidates)):
            self.backtrack(ans, [], candidates, i, target)
        return ans

# @lc code=end

