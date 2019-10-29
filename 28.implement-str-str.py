#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    # def strStr(self, haystack: str, needle: str) -> int:
    #     #print(haystack)
    #     #print(needle)
    #     index = -1
    #     i = j = 0
    #     l_nd = len(needle)
    #     l_hs = len(haystack)
    #     if l_nd == 0:
    #         return 0
        
    #     while i < l_hs:
    #         #print("i:", i)
    #         k = i
    #         j = 0
    #         while j < l_nd and k < l_hs:
    #             #print("k:", k, "j:", j, "char:", haystack[k], "char:", needle[j])
    #             if haystack[k] == needle[j]:
    #                 k += 1
    #             else:
    #                 break
    #             j += 1
    #         #print("l_nd:", l_nd)
    #         #print("i:", i)
    #         if j == l_nd:
    #             return i

    #         i += 1
    #     return -1
    def strStr(self, haystack: str, needle: str) -> int:
        print(haystack)
        print(needle)
        index = -1
        i = j = 0
        l_nd = len(needle)
        l_hs = len(haystack)
        if l_nd == 0:
            return 0

        #while i < l_hs-l_nd+1:
        while i < l_hs:
            if j >= l_nd:
                break
            if index == -1 and i > l_hs-l_nd:
                break
            # print(
            #     "i:", i, "j:", j,
            #     "index:", index, "end:", l_hs-l_nd,
            #     "char:", haystack[i], "char:", needle[j],
            # )
            
            if haystack[i] == needle[j]:
                if index == -1:
                    index = i
                i += 1
                j += 1
            else:
                if index != -1:
                    i = index + 1
                else:
                    i += 1
                j = 0
                index = -1
        return index

# @lc code=end

s = Solution()
print("rst:", s.strStr("hello", "ll"))
print()
print("rst:", s.strStr("aaaaaa", "bba"))
print()
print("rst:", s.strStr("mississippi", "issip"))
print()
print("rst:", s.strStr("aaaaaa", "ab"))
print()