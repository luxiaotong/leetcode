#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = curr = ListNode(None)
        while l1 and l2:
            #print(l1.val)
            #print(l2.val)
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            else:
                curr.next = l2
                l2 = l2.next
                curr = curr.next
        curr.next = l1 or l2
        return l.next

# @lc code=end

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

def printListNode(l: ListNode):
    arr = []
    while l:
        arr.append(l.val)
        l = l.next
    print("->".join(str(e) for e in arr))

s = Solution()
l = s.mergeTwoLists(l1, l2)
printListNode(l)