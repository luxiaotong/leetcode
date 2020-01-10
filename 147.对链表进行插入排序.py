#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#
# https://leetcode-cn.com/problems/insertion-sort-list/description/
#
# algorithms
# Medium (61.68%)
# Likes:    108
# Dislikes: 0
# Total Accepted:    17.5K
# Total Submissions: 28.4K
# Testcase Example:  '[4,2,1,3]'
#
# 对链表进行插入排序。
# 
# 
# 插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
# 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。
# 
# 
# 
# 插入排序算法：
# 
# 
# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
# 
# 
# 
# 
# 示例 1：
# 
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 
# 
# 示例 2：
# 
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        node = head.next
        start = dummy
        end = head
        while node:
            p = start
            while p.next != end:
                if p.next.val > node.val:
                    temp = p.next
                    p.next = node
                    end.next = node.next
                    node.next = temp
                    node = end
                    break
                p = p.next
            if p.next == end:
                if p.next.val <= node.val:
                    end = node
                else:
                    temp = p.next
                    p.next = node
                    temp.next = node.next
                    node.next = temp
                    node = end
            node = node.next
            
        return dummy.next
# @lc code=end

# [-1,5,3,4,0]