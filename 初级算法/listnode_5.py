#!/usr/bin/python
#coding:utf-8
# 请判断一个链表是否为回文链表。
# https://blog.csdn.net/weixin_36372879/article/details/82596003
# 1. 采用快慢指针来找到链表中点
# 2. 找到中点之后，采用空间复杂度O(1)的反转链表的算法，将链表反转，需要注意的是，反转过程中语句的顺序，
# head = head.next一定要在第二句，而不是最后，要不然就断链了，因为p指向了head更改p相当于更改了head,当head指向next之后，才能更改p


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        # 慢指针每次只走一步，快指针走两步
        # 这样快指针走完时，慢指针刚好走完一半
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        new_head = self.ReverseList(slow)
        while new_head:
            if head.val != new_head.val:
                return False
            head = head.next
            new_head = new_head.next
        return True

    def ReverseList(self, head):
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
            #head = head.next
        return new_head

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
head = s.createListnode([1,2,3,3,2,1])
# s.dump(head)
# re = s.ReverseList(head)
# s.dump(re)
res = s.isPalindrome(head)
print(res)