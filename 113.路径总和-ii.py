#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# https://leetcode-cn.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (57.88%)
# Likes:    148
# Dislikes: 0
# Total Accepted:    25.6K
# Total Submissions: 44.1K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
# 
# 
# 返回:
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
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
    def deep_path(self, root:TreeNode, sums: int, ans = [], nums = []):
        if root == None:
            return
        if not root.left and not root.right:
            nums.append(root.val)
            if sum(nums) == sums:
                ans.append(nums)
            return
        if root.left:
            l_nums = nums[:]
            l_nums.append(root.val)
            self.deep_path(root.left, sums, ans, l_nums)
        if root.right:
            r_nums = nums[:]
            r_nums.append(root.val)
            self.deep_path(root.right, sums, ans, r_nums)
        return
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return None
        ans = []
        self.deep_path(root, sum, ans, [])
        return ans
# @lc code=end

