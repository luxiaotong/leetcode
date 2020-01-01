#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []

        result = []
        node_stack = []
        node = root
        while node or node_stack != []:
            while node != None:
                node_stack.append(node)
                node = node.left
            node = node_stack.pop()
            result.append(node.val)
            node = node.right
            
        return result
# @lc code=end

