#!/usr/bin/python
#coding:utf-8
# 新建链表，对比两个链表指针，小的放新链表中，直到某条链表结束，
# 将另一条链表剩余部分接入新链表

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newHead = ListNode(0)
        pre = newHead
        while l1 and l2:
            if l1.val<l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        if l1:
            pre.next = l1
        elif l2:
            pre.next = l2
        return newHead.next

    def createListnode(self, list):
        head = ListNode(list[0])
        p = head
        for i in list[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return head

    def dump(self, head):
        while head:
            print (head.val),
            head = head.next
        print("")
            
s = Solution()
# 有序链表
head1 = s.createListnode([1,2,3])
head2 = s.createListnode([4,5,6])
s.dump(head1)
s.dump(head2)

res = s.mergeTwoLists(head1,head2)
s.dump(res)