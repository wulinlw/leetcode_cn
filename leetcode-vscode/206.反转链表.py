#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (67.29%)
# Likes:    839
# Dislikes: 0
# Total Accepted:    188.4K
# Total Submissions: 277K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        new = None
        while head:
            tmp = head.next
            head.next = new
            new = head 
            head = tmp 
        return new
    
    def reverseList2(self, head: ListNode) -> ListNode:
        if not head or not head.next:return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
# @lc code=end

