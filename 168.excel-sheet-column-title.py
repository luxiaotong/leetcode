#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        arr = []
        while n > 0:
            x = (n-1)%26+1
            s = chr(64+x)
            #print(x, s)
            arr.append(s)
            if n % 26 == 0:
                if n == 26:
                    break
                else:
                    n = n - 26
            n = n//26
        arr.reverse()
        return "" . join(arr)
# @lc code=end

s = Solution()
for i in range(0, 52):
    j = i+1
#    print("Input: ", j, "Output: ", s.convertToTitle(j))

print("Input: 26, Output: ", s.convertToTitle(26))
print("Input: 28, Output: ", s.convertToTitle(28))
print("Input: 701, Output: ", s.convertToTitle(701))
print("Input: 52, Output: ", s.convertToTitle(52))