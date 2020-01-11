#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#
# https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (69.61%)
# Likes:    130
# Dislikes: 0
# Total Accepted:    16.1K
# Total Submissions: 23.1K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
# 
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
# 
# 示例:
# 
# 给定的有序链表： [-10, -3, 0, 5, 9],
# 
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)

        dummy = ListNode(0)
        dummy.next = head
        slow = fast = head
        prev = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            prev = prev.next
        
        mid = slow
        left = head
        right = slow.next
        prev.next = None
        slow.next = None
        # print("mid node:", mid)
        # print("left node:", left)
        # print("right node:", right)

        root = TreeNode(mid.val)
        if left:
            root.left = self.sortedListToBST(left)
        if right:
            root.right = self.sortedListToBST(right)
        return root
# @lc code=end

