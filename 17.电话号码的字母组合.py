#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def backtrack(self, ans, s, arr, pos, N):
        letter_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        if len(s) == N:
            ans.append(s)
            return

        letter_arr = letter_map[arr[pos]]
        for i in range(len(letter_arr)):
            self.backtrack(ans, s+letter_arr[i], arr, pos+1, N)

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        ans = []
        N = len(digits)
        arr = list(digits)
        self.backtrack(ans, "", arr, 0, N)
        return ans
# @lc code=end

