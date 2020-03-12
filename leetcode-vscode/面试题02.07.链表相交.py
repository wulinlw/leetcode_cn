#!/usr/bin/python
#coding:utf-8

# 面试题 02.07. 链表相交
# 给定两个（单向）链表，判定它们是否相交并返回交点。请注意相交的定义基于节点的引用，而不是基于节点的值。换句话说，如果一个链表的第k个节点与另一个链表的第j个节点是同一节点（引用完全相同），则这两个链表相交。

# 示例 1：

# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

# 示例 2：

# 输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# 输出：Reference of the node with value = 2
# 输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

# 示例 3：

# 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# 输出：null
# 输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
# 解释：这两个链表不相交，因此返回 null。

# 注意：

# 如果两个链表没有交点，返回 null 。
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def initlinklist(self, nums):
        head = ListNode(nums[0])
        re = head
        for i in nums[1:]:
            re.next = ListNode(i)
            re = re.next
        return head
    
    def printlinklist(self, head):
        re = []
        while head:
            re.append(head.val)
            head = head.next
        print(re)

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:return None
        l1,l2=headA,headB
        while l1!=l2:
            l1=l1.next if l1 else headB
            l2=l2.next if l2 else headA
        return l1


#
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3        #第一个公共节点
n3.next = n4
n4.next = n5

n2_1 = ListNode(1)
n2_2 = ListNode(2)
n2_1.next = n2_2
n2_2.next = n3      #第一个公共节点

#测试用例需要造一个公共节点，ListNode内存地址是同一个
#不能用2个独立创建的链表
h = o.getIntersectionNode(n1, n2_1)
print(h.val)
# o.printlinklist(h)

