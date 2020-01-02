#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        count = 0
        level = 0
        result = []
        level_result = []
        node_queue = []
        node_queue.append(root)
        while node_queue:
            # count += 1
            # level = math.floor(math.log2(count))
            count = len(node_queue)
            for i in range(count):
                node = node_queue[0]
                level_result.append(node.val)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
                node_queue.remove(node)
            result.append(level_result)
            level_result = []
        
        return result
            

        
# @lc code=end

