#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from typing import List

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pos = 0
        rst = ""
        
        if len(strs) == 0:
            return rst
        
        strs.sort()
        shortest = strs[0]
        for pos in range(len(shortest)):
            tmp = ""
            for i in range(len(strs)):
                if len(strs[i]) == 0:
                    return strs[i]
                elif tmp == "":
                    tmp = strs[i][pos]
                elif tmp == strs[i][pos]:
                    continue
                else:
                    return rst
            rst += tmp
        return rst
# @lc code=end

s = Solution()
print('["flower","flow","flight"]:',s.longestCommonPrefix(["flower","flow","flight"]))
print('[]:', s.longestCommonPrefix([]))
print('[""]:', s.longestCommonPrefix([""]))
print('["", ""]:', s.longestCommonPrefix(["", ""]))
print('["c", "c"]:', s.longestCommonPrefix(["c", "c"]))