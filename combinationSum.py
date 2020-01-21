class Solution:
    def backtrack(self, ans, combo, candidates, pos, target):
        num = sum(combo)+candidates[pos]
        #print("sum:", combo, candidates[pos], num)

        if num == target:
            combo.append(candidates[pos])
            ans.append(combo)
            return
        elif num < target:
            combo.append(candidates[pos])
            for i in range(pos, len(candidates)):
                self.backtrack(ans, combo[:], candidates, i, target)

    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        candidates = sorted(candidates)
        ans = []
        for i in range(len(candidates)):
            self.backtrack(ans, [], candidates, i, target)
        return ans


s = Solution()
print(s.combinationSum([2,3,6,7], 7))
print(s.combinationSum([2,3,5], 8))
