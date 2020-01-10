#
# @lc app=leetcode.cn id=237 lang=python3
#
# [237] 删除链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        n1 = node
        n2 = node.next
        while n2.next:
            n1.val = n2.val
            n1 = n1.next
            n2 = n2.next
        n1.val = n2.val
        n1.next = None
        
# @lc code=end

