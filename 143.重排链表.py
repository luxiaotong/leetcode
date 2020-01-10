#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# https://leetcode-cn.com/problems/reorder-list/description/
#
# algorithms
# Medium (53.78%)
# Likes:    140
# Dislikes: 0
# Total Accepted:    13.9K
# Total Submissions: 25.9K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 示例 1:
# 
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
# 
# 示例 2:
# 
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(self, head) -> ListNode:
        if head == None:
            return None
        r_head = ListNode(head.val)
        p = head.next
        while p:
            new_node = ListNode(p.val)
            new_node.next = r_head
            r_head = new_node
            p = p.next

        return r_head

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None: return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        right = self.reverse(mid)
        slow.next = None

        left = head
        while right:
            new_node = ListNode(right.val)
            new_node.next = left.next
            left.next = new_node
            right = right.next
            left = left.next.next

# @lc code=end

