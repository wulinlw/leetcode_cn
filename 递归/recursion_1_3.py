#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/orignial/card/recursion-i/256/principle-of-recursion/1201/
# 两两交换链表中的节点
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# 示例:
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
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

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

    # 测试打印
    def printList(self, list_node):
        re = []
        while list_node:
            re.append(list_node.val)
            list_node = list_node.next
        print(re)

    # https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/bi-jiao-zhi-jie-gao-xiao-de-zuo-fa-han-tu-jie-by-w/
    def swapPairs(self, head):
        thead = ListNode(-1)
        thead.next = head
        c = thead
        while c.next and c.next.next:
            a, b=c.next, c.next.next
            c.next, a.next = b, b.next
            b.next = a
            c = c.next.next
        return thead.next
    
    def swapPairs2(self, head):
        new = ListNode(0)
        new.next = head
        re = new
        while new.next and new.next.next:
            a,b = new.next, new.next.next
            a.next = b.next
            new.next = b
            b.next = a
            new = new.next.next
        return re.next
        
    #其他方式
    https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/dong-hua-yan-shi-24-liang-liang-jiao-huan-lian-bia/



s = [1,2,3,4]
S = Solution()
l = S.list_generate(s)
S.printList(l)
new = S.swapPairs2(l)
S.printList(new)

