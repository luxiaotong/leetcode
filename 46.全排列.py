#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def backtrack(self, ans, nums, a, b):
        combo = nums[:]
        combo[a], combo[b] = combo[b], combo[a]
        ans.append(combo)

        for i in range(a+2, len(nums)):
            self.backtrack(ans, combo, a+1, i)

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(0, len(nums)):
            self.backtrack(ans, nums, 0, i)
        return ans
        
# @lc code=end

