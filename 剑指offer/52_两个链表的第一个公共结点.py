#!/usr/bin/python
#coding:utf-8

# // 面试题52：两个链表的第一个公共结点
# // 题目：输入两个链表，找出它们的第一个公共结点。
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, head1, head2):
        if not head1 or not head2:return False
        p1 = head1
        p2 = head2
        while True:
            if p1 == p2:
                return p1
            if not p1.next:
                p1.next = head2
            p1 = p1.next
            if not p2.next:
                p2.next = head1
            p2 = p2.next
        return False
        


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3        #第一个公共节点
n3.next = n4
n4.next = n5

n2_1 = ListNode(1)
n2_2 = ListNode(2)
n2_1.next = n2_2
n2_2.next = n3      #第一个公共节点


obj = Solution()
print(obj.FindFirstCommonNode(n1, n2_1).val)