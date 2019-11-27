#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/46/
# 环形链表
# 给定一个链表，判断链表中是否有环。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# 示例 1：
# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。

# 示例 2：
# 输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。

# 示例 3：
# 输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。

# 进阶：
# 你能用 O(1)（即，常量）内存解决此问题吗？


# 给定一个链表，判断链表中是否有环。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# 解法
# 快慢指针，当指向的节点相等时（val，next都相等），就是存在环了
# https://blog.csdn.net/qq_34364995/article/details/80518191

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

    def createListnode(self, list):
        head = ListNode(list[0])
        p = head
        for i in list[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return head

    # 测试打印
    def printList(self, list_node):
        re = []
        while list_node:
            re.append(list_node.val)
            list_node = list_node.next
        print(re)
            
# s = Solution()
# head = s.createListnode([1,2,3,3])
# # s.dump(head)
# res = s.hasCycle(head)
# print(res)

s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l4.next =l3#环
l3.next =l4
l2.next =l3
l1.next =l2
# s.dump(head)
res = s.hasCycle(l1)
print(res)