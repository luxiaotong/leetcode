#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None:
            return None
        h1 = h2 = None
        p = head
        while p:
            if p.val < x:
                if h1 == None:
                    h1 = ListNode(p.val)
                    p1 = h1
                else:
                    n1 = ListNode(p.val)
                    p1.next = n1
                    p1 = p1.next
            else:
                if h2 == None:
                    h2 = ListNode(p.val)
                    p2 = h2
                else:
                    n2 = ListNode(p.val)
                    p2.next = n2
                    p2 = p2.next
            p = p.next
            
        if h1 and h2:
            p1.next = h2
            return h1
        elif h1:
            return h1
        elif h2:
            return h2
        else:
            return None
# @lc code=end

