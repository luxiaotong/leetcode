class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if str == "":
            return 0
        ans = 0
        stack = []
        for i in range(len(s)):
            #print("i", i, s[i], stack)
            if s[i] == "(":
                stack.append(s[i])
            elif s[i] == ")":
                if stack != [] and stack.pop() == "(":
                    ans += 2

        return ans

s = Solution()
#print(s.longestValidParentheses("()()"))
#print(s.longestValidParentheses("(()"))
#print(s.longestValidParentheses(")()())"))
print(s.longestValidParentheses("()(()"))
