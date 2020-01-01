#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        node_stack = []
        result = []
        node_stack.append(root)
        while node_stack != []:
            node = node_stack.pop()
            result.append(node.val)
            if node.right != None:
                node_stack.append(node.right)
            if node.left != None:
                node_stack.append(node.left)
        return result

# @lc code=end

