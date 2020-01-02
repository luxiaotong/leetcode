#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isMirror(self, lnode: TreeNode, rnode: TreeNode) -> bool:
        if lnode == None and rnode == None:
            return True
        if lnode == None or rnode == None or lnode.val != rnode.val:
            return False
        return self.isMirror(lnode.left, rnode.right) and self.isMirror(lnode.right, rnode.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.isMirror(root.left, root.right)
# @lc code=end

