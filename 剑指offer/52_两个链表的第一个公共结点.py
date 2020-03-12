#!/usr/bin/python
#coding:utf-8

# // 面试题52：两个链表的第一个公共结点
# // 题目：输入两个链表，找出它们的第一个公共结点。
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None
class Solution:
    # head1 + head2 =下面的
    # head2 + head1
    def FindFirstCommonNode(self, head1, head2):
        if not head1 or not head2:return False
        l1,l2=head1,head2
        while l1!=l2:
            l1=l1.next if l1 else head2
            l2=l2.next if l2 else head1
        return l1
        


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