#!/usr/bin/python
#coding:utf-8

# 面试题 02.04. 分割链表
# 编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。
# 分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。

# 示例:
# 输入: head = 3->5->8->5->10->2->1, x = 5
# 输出: 3->1->2->10->5->5->8
# https://leetcode-cn.com/problems/partition-list-lcci/



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
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

    def partition(self, head: ListNode, x: int) -> ListNode:
        i, j = head, head
        while j:
            if j.val < x:   # 如果等于 x 不做处理
                i.val, j.val = j.val, i.val     #链表中的替换，原位置的next不变
                i = i.next
            j = j.next
        return head

nums = [3,5,8,5,10,2,1]       
x = 5 
o = Solution()
head = o.initlinklist(nums)
o.printlinklist(head)

h = o.partition(head, x)
# print(h)
o.printlinklist(h)



