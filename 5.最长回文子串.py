#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def expandAroundCenter(self, s, L, R):
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return s[L+1:R], R - L - 1

    def longestPalindrome(self, s: str) -> str:
        if s == "": return s
        max_len = 1
        max_sub = s[0]
        for i in range(len(s)):
            palindrome_odd, len_odd = self.expandAroundCenter(s, i, i)
            palindrome_even, len_even = self.expandAroundCenter(s, i, i+1)
            current_sub = palindrome_even if len_even>len_odd else palindrome_odd
            current_len = max(len_odd, len_even)
            if current_len > max_len:
                max_sub = current_sub
                max_len = current_len
        return max_sub
# @lc code=end

s = Solution()
print(s.longestPalindrome('babad'))