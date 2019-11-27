#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/bytedance/244/linked-list-and-tree/1040/
# 排序链表
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

# 示例 1:
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 示例 2:

# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # https://www.jianshu.com/p/d32c580f9ce2
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 快慢指针找到中间点，并切断链表，递归左边和右边
        if not head or not head.next:
            return head
        cut = slow = fast = head
        while fast and fast.next:
            cut = slow
            fast = fast.next.next
            slow = slow.next
        cut.next = None# 这一步就是将整个链表从中间分开 失去这一步 后面将无限循环
        left = self.sortList(head)
        right = self.sortList(slow)
        # print("l")
        # self.dump(left)
        # print("r")
        # self.dump(right)
        return self.merge(left, right)
    
    # 合并链表
    # 从开头和中间开始比较 将两个相比小的排在head后
    def merge(self, left, right):
        m = n = ListNode(0)
        while left and right:
            if left.val <= right.val:
                n.next = left
                left = left.next
            else:
                n.next = right
                right = right.next
            n = n.next
        n.next = left or right#left 或 right还有剩余的部分，放到n后面
        return m.next#返回新链表的下一个，因为当前值是0
    
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

lis = [4,2,1,3]
s = Solution()
head1 = s.createListnode(lis)
s.dump(head1)
res = s.sortList(head1)
s.dump(res)







