#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, node: TreeNode) -> int:
        if node == None:
            return 0
        return max(self.maxDepth(node.left),self.maxDepth(node.right))+1

    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        if abs(left_depth-right_depth) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
# @lc code=end

