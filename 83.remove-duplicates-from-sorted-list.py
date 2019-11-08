#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        l = head
        while l is not None and l.next is not None:
            if l.val == l.next.val:
                l.next = l.next.next
            else:
                l = l.next
        return head

# @lc code=end

def print_link(head: ListNode):
    l = head
    while l is not None:
        print(l.val, "->")
        l = l.next
    


s = Solution()

l = ListNode(1)
l.next = ListNode(1)
l.next.next = ListNode(2)

print("Input: 1->1->2")
print("Output: ", print_link(s.deleteDuplicates(l)))

l2 = ListNode(1)
l2.next = ListNode(1)
l2.next.next = ListNode(2)
l2.next.next.next = ListNode(3)
l2.next.next.next.next = ListNode(3)
print("Input: 1->1->2->3->3")
print("Output: ", print_link(s.deleteDuplicates(l2)))

l3 = ListNode(1)
l3.next = ListNode(1)
l3.next.next = ListNode(1)
print("Input: 1->1->1")
print("Output: ", print_link(s.deleteDuplicates(l3)))