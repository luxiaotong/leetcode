class Solution:
    def backtrack(self, ans, sub, nums, i):
        if i == len(nums):
            return

        sub.append(nums[i])
        if sub not in ans:
            ans.append(sub)
        else:
            return
        print("sub:", sub)
        print("ans:", ans)
        print()
        for j in range(i+1, len(nums)):
            self.backtrack(ans, sub[:], nums, j)
        return

    def subsetsWithDup(self, nums: [int]) -> [[int]]:
        nums = sorted(nums)
        ans = []
        ans.append([])
        for i in range(len(nums)):
            self.backtrack(ans, [], nums, i)
        return ans

s = Solution()
#print(s.subsetsWithDup([1,2,2]))
print(s.subsetsWithDup([4,4,4,1,4]))
print([[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]])
