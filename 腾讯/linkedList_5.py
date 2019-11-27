#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/tencent/222/linked-list/915/
# 旋转链表
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

# 示例 1:

# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 示例 2:

# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL

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

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # base cases
        if not head:
            return None
        if not head.next:
            return head
        
        # 遍历连表，
        old_tail = head
        n = 1#记录链表长度
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head#尾巴和头连起来,变成环形
        
        # find new tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        new_tail = head
        # print(head.val)
        #找到新的尾巴
        for _ in range(n - k % n - 1):
            # print(i)
            new_tail = new_tail.next
        new_head = new_tail.next#新尾巴的下一个就是新头
        
        # break the ring
        new_tail.next = None
        return new_head


head = [1,2,3,4,5]
k = 2

obj = Solution()
l = obj.createListnode(head)
r = obj.rotateRight(l,k)
print("\n")
obj.dump(r)
# r = obj.deleteNode(node)
# print r