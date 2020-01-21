#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
# https://leetcode-cn.com/problems/multiply-strings/description/
#
# algorithms
# Medium (41.10%)
# Likes:    252
# Dislikes: 0
# Total Accepted:    39.1K
# Total Submissions: 94.8K
# Testcase Example:  '"2"\n"3"'
#
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# 
# 示例 1:
# 
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 
# 示例 2:
# 
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 
# 说明：
# 
# 
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
# 
# 
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        i = len(num1)-1
        j = len(num2)-1
        num3 = ""
        carry = 0
        while i>=0:
            while j>=0:
                temp = carry + int(num1[i]) * int(num2[j])
                carry = temp // 10
                num = temp % 10
                num3 += str(num)
                j -= 1
            i -= 1
            
        return num3
# @lc code=end

