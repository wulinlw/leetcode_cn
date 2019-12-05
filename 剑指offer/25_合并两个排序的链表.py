#!/usr/bin/python
#coding:utf-8

# // 面试题24：反转链表
# // 题目：定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的
# // 头结点。
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

    def Merge(self, h1, h2):
        if not h1 and not h2: return False
        if not h1: return h2
        if not h2: return h1
        new = head = ListNode(0)
        while h1 and h2:
            if h1.val < h2.val: 
                head.next = h1
                h1 = h1.next
            else: 
                head.next = h2
                h2 = h2.next
            head = head.next
        while h1:
            head.next = h1
            h1 = h1.next
        while h2:
            head.next = h2
            h2 = h2.next
        return new.next
        

        


nums1 = [1,2,3,5]
nums2 = [3,4,5]
obj = Solution()
head1 = obj.initlinklist(nums1)
head2 = obj.initlinklist(nums2)
obj.printlinklist(head1)
obj.printlinklist(head2)
h2 = obj.Merge(head1, head2)
obj.printlinklist(h2)


