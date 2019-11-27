#!/usr/bin/python
# coding:utf-8


# https://leetcode-cn.com/explore/learn/card/linked-list/197/conclusion/764/
# 扁平化多级双向链表
# 您将获得一个双向链表，除了下一个和前一个指针之外，它还有一个子指针，可能指向单独的双向链表。这些子列表可能有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。
# 扁平化列表，使所有结点出现在单级双链表中。您将获得列表第一级的头部。

# 示例:
# 输入:
#  1---2---3---4---5---6--NULL
#          |
#          7---8---9---10--NULL
#              |
#              11--12--NULL

# 输出:
# 1-2-3-7-8-11-12-9-10-4-5-6-NULL

# 以上示例的说明:
# 给出以下多级双向链表:
# 我们应该返回如下所示的扁平双向链表:


# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def list_generate(self, lst):
        """
        生成链表
        """
        if not lst:
            return None
        list_node = Node(lst[0])
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

    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        p = rst = Node(None, None, None, None)  # 初始化结果链表及其指针
        visited = head and [head]  # 初始化栈
        while visited:
            vertex = visited.pop()
            if vertex.next:
                visited.append(vertex.next)
            if vertex.child:
                visited.append(vertex.child)
            p.next = vertex  # pop出来的节点就是所需节点
            p, p.prev, p.child = p.next, p, None  # 设定节点属性
            # p = p.next后相当于右移一位后，p.prev就是p了
        if rst.next:
            rst.next.prev = None  # rst是要返回的头，rst.next的prev属性要设为None
        return rst.next


l = [1, 2, 6, 3, 4, 5, 6]
node = 6
obj = Solution()
head = obj.list_generate(l)
obj.printList(head)
r = obj.flatten(head)
obj.printList(r)
