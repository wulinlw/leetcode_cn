#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/31/linked-list/84/
# 相交链表
# 编写一个程序，找到两个单链表相交的起始节点。

# 如下面的两个链表：
# 在节点 c1 开始相交。

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
# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# https://blog.csdn.net/qiubingcsdn/article/details/82619768
class Solution(object):
    # 将headA变为字典，然后判断headB中节点是否在字典中存在
    def getIntersectionNode0(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        cpmDic = {}#这里存的是内测地址
        while headA is not None:
            cpmDic[headA] = 1
            headA = headA.next
        while headB is not None:
            if cpmDic.has_key(headB):
                return headB
            headB = headB.next
        return None
    
    # 双指针法，时间复杂度O(n)，额外未申请空间（参考他人代码）
    # 双指针法，制定两个指针pA pB,分别用这两个指针遍历A+B,如果两个指针在某点相遇，则该点就是链表的交点
    # A=[1,3,5,9,11]    1,3,5,9,11,2,4,6,8,9,11     #A+B
    # B=[2,4,6,8,9,11]  2,4,6,8,9,11,1,3,5,9,11     #B+A
    # A+B的链表长度是一定的，如果有交点，那么这个长链表从后向前看的前几个必定是相同的
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        tempA = headA
        tempB = headB
        while tempA!=tempB:
            # print(tempA.val,tempB.val)
            tempA = tempA.next
            tempB = tempB.next
            if not tempA and not tempB:
                return None
            #这样补一下，最后长度都是A+B，如有有公共尾巴，最后几位都是相等的
            if not tempA:     #A链表后面接上B链表
                tempA = headB
            if not tempB:     #B链表后面接上A链表
                tempB = headA
        return tempA

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

    def join(self, head1,head2):
        while head1:
            if head1.next == None:
                head1.next = head2
                return head1
            head1 = head1.next


s = Solution()
head1 = s.createListnode([1,3])
head2 = s.createListnode([2,4,6,8])
comm = s.createListnode([9,11])#这一题需要弄一个相同的尾巴，内存地址是同一个
s.dump(head1)
s.dump(head2)
s.join(head1,comm)
s.join(head2,comm)
s.dump(head1)
s.dump(head2)
r = s.getIntersectionNode(head1,head2)
s.dump(r)
