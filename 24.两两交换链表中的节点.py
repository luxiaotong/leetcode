#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy
        while p2.next and p2.next.next:
            p2 = p2.next.next

            # 交换
            tmp = p1.next
            p1.next = p2
            tmp.next = p2.next
            p2.next = tmp

            p1 = p1.next.next
            p2 = p1

        return dummy.next

# @lc code=end

