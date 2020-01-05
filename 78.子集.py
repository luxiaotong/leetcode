#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def backtrack(self, ans, sub, nums, i):
        if i == len(nums):
            return
        sub.append(nums[i])
        ans.append(sub)
        for j in range(i+1, len(nums)):
            self.backtrack(ans, sub[:], nums, j)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ans.append([])
        for i in range(len(nums)):
            self.backtrack(ans, [], nums, i)
        return ans

# @lc code=end

