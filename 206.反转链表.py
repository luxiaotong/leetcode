#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return []
        p = ListNode(head.val)
        n = head.next
        while n:
            new_node = ListNode(n.val)
            new_node.next = p
            p = new_node
            n = n.next
        return p
# @lc code=end

