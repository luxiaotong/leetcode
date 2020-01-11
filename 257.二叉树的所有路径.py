#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# https://leetcode-cn.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (61.34%)
# Likes:    184
# Dislikes: 0
# Total Accepted:    21.7K
# Total Submissions: 35.4K
# Testcase Example:  '[1,2,3,null,5]'
#
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 输入:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# 输出: ["1->2->5", "1->3"]
# 
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
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
    def deep_path(self, root: TreeNode, s: str, ans = []):
        if root == None:
            return
        if not root.left and not root.right:
            s += str(root.val)
            ans.append(s)
            return
        if root.left:
            sl = s + str(root.val) + '->'
            self.deep_path(root.left, sl, ans)
        if root.right:
            sr = s+ str(root.val) + '->'
            self.deep_path(root.right, sr, ans)
        return
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root == None:
            return []
        ans = []
        self.deep_path(root, '', ans)
        return ans
# @lc code=end

