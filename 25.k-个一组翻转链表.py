#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(self, head):
        r_node = tail = ListNode(head.val)
        p = head
        p = p.next
        while p:
            new_node = ListNode(p.val)
            new_node.next = r_node
            r_node = new_node
            head = new_node
            p = p.next
        return r_node, tail

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None: return []
        dummy = ListNode(0)
        dummy.next = head

        prev = end = dummy
        while end.next:
            i = k
            while i and end:
                i = i - 1
                end = end.next
            if end == None: break

            start = prev.next
            p = end.next
            end.next = None
            prev.next, start = self.reverse(start)

            #print("start, end, next", start.val, end.val, p.val)
            
            start.next = p
            prev = end = start

            n = dummy
            while n:
                print("dummy:", n.val, end=",")
                n = n.next
            print()
        return dummy.next

        
# @lc code=end

