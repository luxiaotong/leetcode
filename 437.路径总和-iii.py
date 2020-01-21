#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#
# https://leetcode-cn.com/problems/path-sum-iii/description/
#
# algorithms
# Easy (52.98%)
# Likes:    262
# Dislikes: 0
# Total Accepted:    17.5K
# Total Submissions: 32.9K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# 给定一个二叉树，它的每个结点都存放着一个整数值。
# 
# 找出路径和等于给定数值的路径总数。
# 
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
# 
# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
# 
# 示例：
# 
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
# 
# 返回 3。和等于 8 的路径有:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11
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
    def deep_path(self, root: TreeNode, sums: int, ans: int, nums):
        if root == None: return

        nums.append(root.val)
        print("nums:", nums, sum(nums))
        if sum(nums) == sums:
            ans.append(nums)
            nums = []
            return
        print("ans:", ans)
        if root.left:
            l_nums = nums[:]
            self.deep_path(root.left, sums, ans, l_nums)
            self.deep_path(root.left, sums, ans, [])
        if root.right:
            r_nums = nums[:]
            self.deep_path(root.right, sums, ans, r_nums)
            self.deep_path(root.right, sums, ans, [])
        return
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root == None: return 0
        ans = []
        self.deep_path(root, sum, ans, [])
        return len(ans)
# @lc code=end

# [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22
# [-2,null,-3]\n-5
# [0,1,1]\n1
# [1,null,2,null,3,null,4,null,5]\n3
# [1,-2,-3,1,3,-2,null,-1]\n3