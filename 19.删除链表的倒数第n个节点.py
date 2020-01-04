#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy
        for i in range(n+1):
            p2 = p2.next
        while p2:
            p1 = p1.next
            p2 = p2.next
        
        p1.next = p1.next.next

        return dummy.next
# @lc code=end

