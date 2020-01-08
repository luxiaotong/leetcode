#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def islegal(self, c):
        if c >= 'a' and c <= 'z' or c >= '0' and c <= '9':
            return True
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s)-1
        while i < j:
            print("i, j:", i, j)
            print("s:", s[i], s[j])
            if self.islegal(s[i]) and self.islegal(s[j]):
                if s[i] == s[j]:
                    print(s[i], s[j])
                    i += 1
                    j -= 1
                else:
                    return False
            elif not self.islegal(s[i]):
                i += 1
                continue
            elif not self.islegal(s[j]):
                j -= 1
                continue
        return True
# @lc code=end

