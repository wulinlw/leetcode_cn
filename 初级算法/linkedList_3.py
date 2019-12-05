#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/43/
# 反转链表
# 反转一个单链表。

# 示例:

# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

# 把当前链表的下一个节点pCur插入到头结点的下一个节点中，就地反转。
# 1->2->3->4->5 的就地反转过程：
# 2->1->3->4->5
# 3->2->1->4->5
# 4>-3->2->1->5
# 5->4->3->2->1
import sys
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

    def show(self, head):
        re = []
        while head:
            re.append(head.val)
            head = head.next
        print(re,"\n")

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 图形理解
        # https://blog.csdn.net/qq_42351880/article/details/88637387
        if head is None: return None
        newHead = None
        while head:
            temp = head.next    #后面节点放入temp
            head.next = newHead #新连表newHead放入当前节点的next
            newHead = head      #当前节点放入newHead,和上一步可理解为交换节点
            # self.show(newHead)
            head = temp         #后面节点继续循环
            print(newHead.val)
        return newHead



head = [1,2,3,4,5]
obj = Solution()
l = obj.list_generate(head)
obj.show(l)
r = obj.reverseList(l)
obj.show(r)



