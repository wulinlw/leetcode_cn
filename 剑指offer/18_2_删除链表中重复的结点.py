#!/usr/bin/python
#coding:utf-8

# 删除链表中重复的结点
# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
# 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
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

    def deleteDuplication(self, head):
        if not head :return None
        p = head
        pre = None
        while p and p.next:
            if p.val == p.next.val:     #遇到相同，
                pre = p                 #保留第一个
                sameVal = p.val
                while sameVal == p.val: #跳过所有相同的
                    p = p.next
                pre.next = p            #连接下一个不同的
            else:
                pre = p
                p = p.next
        return head




nums = [1,1,2,3,3,4,5,5,6]
obj = Solution()
head = obj.initlinklist(nums)

obj.deleteDuplication(head)
obj. printlinklist(head)