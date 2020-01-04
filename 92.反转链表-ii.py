#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head == None:
            return None

        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        i = 0
        while node:
            if i == m-1:
                p1 = node
            if i == n:
                p2 = node
            i += 1
            node = node.next

        p3 = p1.next
        r_node = ListNode(p3.val)
        r_node.next = p2.next
        for i in range(n-m):
            p3 = p3.next
            new_node = ListNode(p3.val)
            new_node.next = r_node
            r_node = new_node
        
        new_head = r_node
        p1.next = new_head
        return dummy.next


# @lc code=end

