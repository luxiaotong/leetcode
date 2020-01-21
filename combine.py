class Solution:
    def backtrack(self, ans, combo, num, n, k):
        combo.append(num)
        if len(combo) == k:
            ans.append(combo)
            return
        for i in range(num+1, n+1):
            self.backtrack(ans, combo[:], i, n, k)

    def combine(self, n: int, k: int) -> [[int]]:
        ans = []
        for i in range(1, n+1):
            self.backtrack(ans, [], i, n, k)
        return ans

s = Solution()
print(s.combine(4, 2))
