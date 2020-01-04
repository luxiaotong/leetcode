#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next == None:
            return head
        
        node = head
        n = 1
        while node.next:
            n += 1
            node = node.next
        node.next = head

        node2 = head
        for i in range(n - k%n - 1):
            node2 = node2.next
        new_head = node2.next
        node2.next = None
        return new_head

# @lc code=end

