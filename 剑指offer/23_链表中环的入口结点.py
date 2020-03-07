#!/usr/bin/python
#coding:utf-8

# // 面试题23：链表中环的入口结点
# // 题目：一个链表中包含环，如何找出环的入口结点？例如，在图3.8的链表中，
# // 环的入口结点是结点3。
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

    def MeetingNode(self, head):
        if not head:return False
        p1 = slow = fast = head
        while 1:
            slow = slow.next
            if not fast.next.next:
                return False
            fast = fast.next.next
            if slow == fast:
                break
        while p1 != slow:
            p1 = p1.next
            slow = slow.next
        return slow


        
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n2#环在这里
# print(n5.val,n5.next.val)

nums = [1,2,3,4,5]
obj = Solution()
# head = obj.initlinklist(nums)
# obj.printlinklist(n1)
print(obj.MeetingNode(n1).val)


