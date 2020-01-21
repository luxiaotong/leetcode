#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#
# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (60.49%)
# Likes:    255
# Dislikes: 0
# Total Accepted:    17.1K
# Total Submissions: 28.1K
# Testcase Example:  '3'
#
# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
# 
# 示例:
# 
# 输入: 3
# 输出:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# 解释:
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def gen_tree(self, start, end, ans, path):
        if start > end:
            path.append(None)
            return
        if start == end:
            print("i:", start, end)
            path.append(start)
            ans.append(path)
            return 

        for i in range(start, end+1):
            print("mid:", i, start, i-1, i+1, end)
            path.append(i)
            print("path1:", path)
            self.gen_tree(start, i-1, ans, path[:])
            self.gen_tree(i+1, end, ans, path[:])
            print("path2:", path)
            # root = TreeNode(i)
            # root.left = self.gen_tree(start, i-1, ans, root)
            # root.right = self.gen_tree(i+1, end, ans, root)
        # print("ans:", ans)
        return
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []
        ans = []
        self.gen_tree(1, n, ans, [])
        return ans
        
# @lc code=end

