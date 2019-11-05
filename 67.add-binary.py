#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        i = len(a)-1
        j = len(b)-1
        rst = []
        while True:
            if i < 0 and j < 0:
                if carry == 1:
                    rst.append(1)
                break
            elif i < 0 and j >= 0:
                num_b = int(b[j])
                if num_b == 1:
                    if carry == 1:
                        rst.append(0)
                        carry = 1
                    else:
                        rst.append(1)
                        carry = 0
                else:
                    rst.append(carry)
                    carry = 0
            elif j < 0 and i >= 0:
                num_a = int(a[i])
                if num_a == 1:
                    if carry == 1:
                        rst.append(0)
                        carry = 1
                    else:
                        rst.append(1)
                        carry = 0
                else:
                    rst.append(carry)
                    carry = 0
            else:
                num_a = int(a[i])
                num_b = int(b[j])
                if num_a == 1 and num_b == 1:
                    if carry == 1:
                        rst.append(1)
                    else:
                        rst.append(0)
                    carry = 1
                elif num_a == 1 or num_b == 1:
                    if carry == 1:
                        rst.append(0)
                        carry = 1
                    else:
                        rst.append(1)
                        carry = 0
                else:
                    if carry == 1:
                        rst.append(1)
                    else:
                        rst.append(0)
                    carry = 0
            i -= 1
            j -= 1
            #print(rst)
        rst.reverse()
        return "".join(str(x) for x in rst)


# @lc code=end

s = Solution()
print('Input: a = "11", b = "1"')
print('Output: ', s.addBinary(a = "11", b = "1"))
print('Input: a = "1010", b = "1011"')
print('Output: ', s.addBinary(a = "1010", b = "1011"))
print('Input: a = "0", b = "0"')
print('Output: ', s.addBinary(a = "0", b = "0"))
print('Input: a = "100", b = "110010"')
print('Output: ', s.addBinary(a = "100", b = "110010"))