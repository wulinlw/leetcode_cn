#!/usr/bin/python
# coding:utf-8

# https://leetcode-cn.com/explore/learn/card/linked-list/195/classic-problems/752/
# 移除链表元素
# 删除链表中等于给定值 val 的所有节点。

# 示例:
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5


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

    # 测试打印
    def printList(self, list_node):
        re = []
        while list_node:
            re.append(list_node.val)
            list_node = list_node.next
        print(re)

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p = ListNode(-1)
        # 因为要删除的可能是链表的第一个元素，所以用一个h节点来做处理
        # 最后只要返回h的下一个节点即可
        p.next, h = head, p
        # 注意遍历的条件是p.next不为空
        while p.next:
            # 如果p的下一个节点的值==val
            # P就指向下下一个，这就删掉了指定的节点
            if p.next.val == val:
                p.next = p.next.next
                # 注意这里的continue
                # 因为循环最后还有一个P=p.next，所以要跳过
                continue
            # 不用continue用else的方式也是可以的
            p = p.next
        return h.next


l = [1, 2, 6, 3, 4, 5, 6]
node = 6
obj = Solution()
head = obj.list_generate(l)
obj.printList(head)
r = obj.removeElements(head, node)
obj.printList(r)
