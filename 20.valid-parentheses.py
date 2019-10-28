#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        elif str == "":
            return True
        
        stack = []

        for i in range(len(s)):
            #print(stack)
            if len(stack) == 0:
                stack.append(s[i])
            else:
                tmp = stack.pop()
                if tmp == '(' and s[i] == ')':
                    continue
                elif tmp == '[' and s[i] == ']':
                    continue
                elif tmp == '{' and s[i] == '}':
                    continue
                else:
                    stack.append(tmp)
                    stack.append(s[i])
        
        if len(stack) == 0:
            return True
        else:
            return False

# @lc code=end

s = Solution()
print('"()":', s.isValid("()"))
print('"()[]{}":', s.isValid("()[]{}"))
print('"(]":', s.isValid("(]"))
print('"([)]":', s.isValid("([)]"))
print('"{[]}":', s.isValid("{[]}"))