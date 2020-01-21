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
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        candidates = sorted(candidates)
        ans = []
        for i in range(len(candidates)):
            self.backtrack(ans, [], candidates, i, target)
        return ans


s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))
print(s.combinationSum2([2,5,2,1,2], 5))

