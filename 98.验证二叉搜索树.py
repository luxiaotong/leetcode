#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (28.17%)
# Likes:    370
# Dislikes: 0
# Total Accepted:    59.5K
# Total Submissions: 210.2K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 
# 假设一个二叉搜索树具有如下特征：
# 
# 
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 
# 
# 示例 1:
# 
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
# 
# 
# 示例 2:
# 
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
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
    def checkBST(self, root, min_val, max_val):
        if root == None:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        return \
            self.checkBST(root.left, min_val, root.val) \
            and \
            self.checkBST(root.right, root.val, max_val)

    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.checkBST(root, -2**32, 2**32-1)

# @lc code=end

# [5,1,4,null,null,3,6]
# [10,5,15,null,null,6,20]
# [1,1]
# [1,null,1]