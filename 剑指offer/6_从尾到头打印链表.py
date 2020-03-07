#!/usr/bin/python
#coding:utf-8

# 从尾到头打印链表
# 输入一个链表，从尾到头打印链表每个节点的值。

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
        

    #不允许修改链表，需要用递归打印
    def printListFromTailToHead(self, head):
        return self.printListFromTailToHead(head.next) + [head.val] if head else []

    #栈
    def printListFromTailToHead2(self, head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]


        
nums = [1,2,3,4,5]
obj = Solution()
re = obj.initlinklist(nums)
# print(re)
# obj.printlinklist(re)
obj.printListFromTailToHead2(re)