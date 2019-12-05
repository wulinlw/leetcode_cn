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
        if head.next:
            self.printListFromTailToHead(head.next)
        print(head.val, "")     #放在后面就是倒着打印了，递归到最后才会输出，一层层网上走

        
nums = [1,2,3,4,5]
obj = Solution()
re = obj.initlinklist(nums)
# print(re)
# obj.printlinklist(re)
obj.printListFromTailToHead(re)