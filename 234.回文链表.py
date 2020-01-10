#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        prev = slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        n = slow
        while n:
            print("slow:", n.val, end=",")
            n = n.next
        print()

        r_head = ListNode(slow.val)
        slow = slow.next
        while slow:
            new_node = ListNode(slow.val)
            new_node.next = r_head
            r_head = new_node
            slow = slow.next

        n = r_head
        while n:
            print("n1:", n.val, end=",")
            n = n.next
        print()

        n = head
        while n:
            print("n2:", n.val, end=",")
            n = n.next
        while head and r_head:
            if head.val != r_head.val:
                return False
            head = head.next
            r_head = r_head.next
        return True
# @lc code=end

