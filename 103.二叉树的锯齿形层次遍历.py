#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (52.93%)
# Likes:    129
# Dislikes: 0
# Total Accepted:    27.9K
# Total Submissions: 52.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# 
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回锯齿形层次遍历如下：
# 
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        
        level = 1
        ans = []
        queue = []
        queue.append(root)
        while queue:
            nums = []
            count = len(queue)
            for i in range(count):
                node = queue.pop(0)
                nums.append(node.val)
                print("nums:", nums)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2 == 0:
                nums = nums[::-1]
            ans.append(nums)
            level += 1
        return ans

        
# @lc code=end

# [0,2,4,1,null,3,-1,5,1,null,6,null,8]