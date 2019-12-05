#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/31/linked-list/83/
# 奇偶链表
# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

# 示例 1:

# 输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
# 示例 2:

# 输入: 2->1->3->5->6->4->7->NULL 
# 输出: 2->3->6->7->1->5->4->NULL
# 说明:

# 应当保持奇数节点和偶数节点的相对顺序。
# 链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #至少有3个
        if head == None or head.next == None or head.next.next == None:
            return head
        
        p = head.next  # 偶数位
        q = head.next.next  # 奇数位
        head.next = q #1，3链接
        t = p  # 记录第一个偶数位
        while q.next:#第4位
            p.next = p.next.next#下一个偶数位
            p = p.next
            q.next = q.next.next#下一个奇数位
            if q.next:  # 下一个奇数非空，才能进行赋值操作
                q = q.next

        q.next = t  # 连上第一个偶数位
        p.next = None  # 偶数位最后一个连上None
        return head


    def createListnode(self, list):
        head = ListNode(list[0])
        p = head
        for i in list[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return head

    def dump(self, head):
        while head:
            print (head.val),
            head = head.next
        print("")



s = Solution()
head1 = s.createListnode([1,2,3,4,5,6,7])
s.dump(head1)
r = s.oddEvenList(head1)
s.dump(r)