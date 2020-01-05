#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def backtrack(self, ans, sub, nums, i):
        if i == len(nums):
            return

        sub.append(nums[i])
        if sub not in ans:
            ans.append(sub)
        else:
            return
        for j in range(i+1, len(nums)):
            self.backtrack(ans, sub[:], nums, j)
        return

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        store = [[]]
        ans = []
        ans.append([])
        for i in range(len(nums)):
            self.backtrack(ans, [], nums, i)
        return ans

# @lc code=end

