#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        result = []
        mid_stack = []
        node_stack = []
        node_stack.append(root)
        while node_stack:
            node = node_stack.pop()
            if node.left:
                node_stack.append(node.left)
            if node.right:
                node_stack.append(node.right)
            mid_stack.append(node)
        while mid_stack:
            mid_node = mid_stack.pop()
            result.append(mid_node.val)
        return result
        
# @lc code=end

