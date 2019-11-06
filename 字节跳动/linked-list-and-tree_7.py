#!/usr/bin/python
#coding:utf-8
import heapq
# https://leetcode-cn.com/explore/interview/card/bytedance/244/linked-list-and-tree/1025/
# 合并K个排序链表
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

# 示例:
# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6

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
        re = []
        while head:
            re.append(head.val),
            head = head.next
        print(re)

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for node in lists:
            if node: 
                heap.append((node.val, node))  # 堆中放入tuple：值，地址
        heapq.heapify(heap)  # 做成堆
        dummy = ListNode(0)
        curr = dummy

        while heap:
            pop = heapq.heappop(heap)  # 从堆中取最小的值
            curr.next = ListNode(pop[0])  # 将值放入
            curr = curr.next
            if pop[1].next:  # 如果该链表没结束
                heapq.heappush(heap, (pop[1].next.val, pop[1].next)) # 将该链表下个节点压入栈中
        return dummy.next
    
    


lists = [
  [1,4,5],
  [1,3,4],
  [2,6]
]
s = Solution()
links = []
for i in lists:
    links.append(s.createListnode(i))
for i in links:
    s.dump(i)
# head1 = s.createListnode(head)
# s.dump(head1)
res = s.mergeKLists(links)
s.dump(res)









