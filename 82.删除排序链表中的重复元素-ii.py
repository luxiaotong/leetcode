#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            p1 = p.next
            p2 = p.next.next
            if p1.val == p2.val:
                if p2.next == None:
                    p.next = p2.next
                elif p2.val == p2.next.val:
                    p.next = p2
                else:
                    p.next = p2.next
            else:
                p = p.next
        return dummy.next
# @lc code=end

