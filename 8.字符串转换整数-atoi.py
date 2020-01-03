#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        sign = 1
        count = 0
        num = 0
        for i in range(len(str)):
            if str[i] == " ":
                if count == 0:
                    continue
                else:
                    break
            if str[i] == "-":
                if count == 0:
                    sign = -1
                    count += 1
                    continue
                else:
                    break
            if str[i] == "+":
                if count == 0:
                    count += 1
                    continue
                else:
                    break
            if ord(str[i]) < 48 or ord(str[i]) > 57:
                if count == 0:
                    return 0
                else: break
            num = num * 10 + int(str[i])
            count += 1
        num = sign * num
        if num > 2 ** 31-1:
            num = 2 ** 31-1
        if num < -2 ** 31:
            num = -2 ** 31
        return num
# @lc code=end

s = Solution()
print(s.myAtoi("42"))
print(s.myAtoi("   -42"))
print(s.myAtoi("4193 with words"))
print(s.myAtoi("words and 987"))
print(s.myAtoi("-91283472332"))
print(s.myAtoi("+1"))
print(s.myAtoi("+0 123"))