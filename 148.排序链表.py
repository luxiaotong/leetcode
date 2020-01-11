#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode-cn.com/problems/sort-list/description/
#
# algorithms
# Medium (62.90%)
# Likes:    365
# Dislikes: 0
# Total Accepted:    35.6K
# Total Submissions: 56.5K
# Testcase Example:  '[4,2,1,3]'
#
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
# 
# 示例 1:
# 
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 
# 
# 示例 2:
# 
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def merge(self, left, right) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        while left and right:
            if left.val <= right.val:
                p.next = ListNode(left.val)
                left = left.next
            else:
                p.next = ListNode(right.val)
                right = right.next
            p = p.next
        while left:
            p.next = ListNode(left.val)
            left = left.next
            p = p.next
        while right:
            p.next = ListNode(right.val)
            right = right.next
            p = p.next
        
        return dummy.next

    def sortList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = head
        prev = dummy
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            prev = prev.next
        if slow == fast:
            return head
        
        left = head
        right = prev.next
        prev.next = None
        
        return self.merge(self.sortList(left), self.sortList(right))
# @lc code=end

