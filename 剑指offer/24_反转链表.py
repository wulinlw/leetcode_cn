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

    def ReverseList(self, head):
        if not head: return None
        new = None
        while head:
            tmp = head.next
            head.next = new
            new = head
            head = tmp
        return new

    #https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/
    def ReverseList2(self, head):
        if not head or not head.next:
            return head 
        cur = self.ReverseList2(head.next)
        head.next.next = head
        head.next = None
        return cur
        


nums = [1,2,3,4,5]
obj = Solution()
head = obj.initlinklist(nums)
obj.printlinklist(head)
h2 = obj.ReverseList(head)
obj.printlinklist(h2)

head = obj.initlinklist(nums)
h3 = obj.ReverseList2(head)
obj.printlinklist(h3)

