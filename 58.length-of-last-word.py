#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str_arr = s.strip().split(" ")
        last_word = str_arr.pop()
        return len(last_word)
# @lc code=end

s = Solution()
print('Input: "Hello World"')
print('Output: ', s.lengthOfLastWord("Hello World"))
print('Input: ""')
print('Output: ', s.lengthOfLastWord(""))
print('Input: " "')
print('Output: ', s.lengthOfLastWord(" "))
print('Input: "Hello "')
print('Output: ', s.lengthOfLastWord("Hello "))