#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# https://leetcode-cn.com/problems/group-anagrams/description/
#
# algorithms
# Medium (59.91%)
# Likes:    245
# Dislikes: 0
# Total Accepted:    45.1K
# Total Submissions: 74.9K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# 
# 示例:
# 
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# 说明：
# 
# 
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
# 
# 
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == []:
            return []
        hashmap = {}
        for s in strs:
            tmp = list(s)
            k = "".join(sorted(tmp))
            # print("k:", k)
            # print("tmp:", tmp)
            # print("s:", s)
            if k in hashmap:
                hashmap[k].append(s)
            else:
                hashmap[k] = [s]
            # print("H:", hashmap)
        ans = []
        for k,v in hashmap.items():
            ans.append(v)
        # print(ans)
        return ans
# @lc code=end

