#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/42/
# 删除链表的倒数第N个节点
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

# 示例：

# 给定一个链表: 1->2->3->4->5, 和 n = 2.

# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：

# 给定的 n 保证是有效的。

# 进阶：

# 你能尝试使用一趟扫描实现吗？

# 典型的利用双指针法解题。
# 首先让指针first指向头节点，然后让其向后移动n步，
# 接着让指针sec指向头结点，并和first一起向后移动。
# 当first的next指针为NULL时，sec即指向了要删除节点的前一个节点，
# 接着让first指向的next指针指向要删除节点的下一个节点即可。
# 注意如果要删除的节点是首节点，那么first向后移动结束时会为NULL，
# 这样加一个判断其是否为NULL的条件，若为NULL则返回头结点的next指针。
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def list_generate(self, lst):
        """
        生成链表
        """
        if not lst:
            return None
        list_node = ListNode(lst[0])
        if len(lst) == 1:
            list_node.next = None
        else:
            list_node.next = self.list_generate(lst[1:])
        return list_node

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = head
        p2 = head
        i = 0
        while i < n:
            p1 = p1.next
            i += 1
        if p1 == None:
            return head.next
        while p1.next != None:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return head


head = [4, 5, 1, 9]
node = 5
obj = Solution()
r = obj.removeNthFromEnd(node)
print r