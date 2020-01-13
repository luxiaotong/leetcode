#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (38.51%)
# Likes:    278
# Dislikes: 0
# Total Accepted:    21.3K
# Total Submissions: 55K
# Testcase Example:  '[1,2,3]'
#
# 给定一个非空二叉树，返回其最大路径和。
# 
# 本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# 输出: 6
# 
# 
# 示例 2:
# 
# 输入: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# 输出: 42
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
        
    def maxPathSum(self, root: TreeNode) -> int:
        if root == None:
            return 0

        def max_path(root):
            nonlocal ans
            if root == None:
                return 0
            l_max = max(0, max_path(root.left))
            r_max = max(0, max_path(root.right))
            m_max = root.val + max(l_max, r_max)
            lmr = root.val + l_max + r_max
            ans = max(ans, max(m_max, lmr))
            print(ans)
            return m_max
        ans = float('-inf')
        max_path(root)
        return ans
# @lc code=end

