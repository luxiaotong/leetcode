#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://blog.csdn.net/weixin_42762089/article/details/86914743

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left != None and root.right != None:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif root.left != None:
            return self.minDepth(root.left)+1
        elif root.right != None:
            return self.minDepth(root.right)+1
        else:
            return 1
# @lc code=end

