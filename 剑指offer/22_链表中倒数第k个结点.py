#!/usr/bin/python
#coding:utf-8

# // 面试题22：链表中倒数第k个结点
# // 题目：输入一个链表，输出该链表中倒数第k个结点。为了符合大多数人的习惯，
# // 本题从1开始计数，即链表的尾结点是倒数第1个结点。例如一个链表有6个结点，
# // 从头结点开始它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个结点是
# // 值为4的结点。
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

    def FindKthToTail(self, head, k):
        if not head or not k: return None
        slow = fast = head
        for i in range(k-1):
            if not fast.next:
                return None
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
            if not fast.next:
                return slow
        

nums = [1,2,3,4,5]
obj = Solution()
#以下是true
head = obj.initlinklist(nums)
obj.printlinklist(head)
print(obj.FindKthToTail(head, 2).val)
print(obj.FindKthToTail(head, 3).val)

