class Solution:
    def backtrack(self, ans, nums, a, b):
        combo = nums[:]
        combo[a], combo[b] = combo[b], combo[a]
        ans.append(combo)
        print("combo:", combo)

        self.backtrack(ans, combo, a+1, i)

        # 需要解决0,0,2,3没有交换的问题
        for i in range(a+2, len(nums)):
            print("a, b:", a+1, i)
            self.backtrack(ans, combo, a+1, i)

    def permute(self, nums: [int]) -> [[int]]:
        ans = []
        for i in range(0, len(nums)):
            print("a, b:", 0, i)
            self.backtrack(ans, nums, 0, i)
        return ans

s = Solution()
#print(s.permute([1,2,3,4]))
print(s.permute([5,4,6,2]))

#[[5,4,6,2],[5,6,4,2],[5,6,2,4],[5,2,6,4],[5,2,4,6],[4,5,6,2],[4,6,5,2],[4,6,2,5],[4,2,6,5],[4,2,5,6],[6,4,5,2],[6,5,4,2],[6,5,2,4],[6,2,5,4],[6,2,4,5],[2,4,6,5],[2,6,4,5],[2,6,5,4],[2,5,6,4],[2,5,4,6]]
#[[5,4,6,2],[5,4,2,6],[5,6,4,2],[5,6,2,4],[5,2,4,6],[5,2,6,4],[4,5,6,2],[4,5,2,6],[4,6,5,2],[4,6,2,5],[4,2,5,6],[4,2,6,5],[6,5,4,2],[6,5,2,4],[6,4,5,2],[6,4,2,5],[6,2,5,4],[6,2,4,5],[2,5,4,6],[2,5,6,4],[2,4,5,6],[2,4,6,5],[2,6,5,4],[2,6,4,5]]
