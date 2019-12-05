#!/usr/bin/python
#coding:utf-8

# 在O(1)时间内删除链表结点
# 给定单向链表的头指针和一个结点指针,定义一个函数在O(1)时间删除该结点
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution:
    def initlinklist(self, nums):
        head = ListNode(nums[0])
        re = head
        for i in nums[1:]:
            re.next = ListNode(i)
            re = re.next
        return head
    
    def printlinklist(self, head):
        re = []
        while head:
            re.append(head.val)
            head = head.next
        print(re)

    def deleteNode(self, head, delNode):
        # print(head, delNode)
        if not head or not delNode:return None
        if delNode == head:return None
        if not delNode.next:#在尾节点
            p = head
            while p.next and p.next.next:
                p = p.next
            p.next = None
        else:
            delNode.val = delNode.next.val
            delNode.next = delNode.next.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

obj = Solution()
# re = obj.initlinklist(nums)

# obj.deleteNode(n1, n3)
# obj.printlinklist(n1)

# print(obj.deleteNode(n1, n1))

obj.deleteNode(n1, n5)
obj.printlinklist(n1) 