#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/bytedance/244/linked-list-and-tree/1023/
# 环形链表 II
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# 说明：不允许修改给定的链表。

# 示例 1：
# 输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。

# 示例 2：
# 输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。

# 示例 3：
# 输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。

# 进阶：
# 你是否可以不用额外空间解决此题？


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
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

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 判断链表是否有环并找到入环节点:（快慢指针）
        # 1、如果快指针走到空，无环
        # 2、如果二者相遇，有环
        # 3、相遇后，慢指针不动，新指针从头开始走
        # 4、两个指针同时走，每次均走一步，相遇点即为入环点
        if not head or not head.next:
            return None
        first = second = head
        while second.next and second.next.next:
            first = first.next
            second = second.next.next
            if first == second:
                p = head
                while first != p:#相遇点距环入口的距离等于头节点距环入口的距离
                    p = p.next
                    first = first.next
                return p
        return None


head = [1,2]
pos = 0
s = Solution()
head1 = s.createListnode(head)
s.dump(head1)
res = s.detectCycle(head1)
s.dump(res)




