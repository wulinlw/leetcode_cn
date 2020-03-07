#!/usr/bin/python
#coding:utf-8

# // 面试题35：复杂链表的复制
# // 题目：请实现函数ComplexListNode* Clone(ComplexListNode* pHead)，复
# // 制一个复杂链表。在复杂链表中，每个结点除了有一个m_pNext指针指向下一个
# // 结点外，还有一个m_pSibling 指向链表中的任意结点或者nullptr。
class Node:
    def __init__(self, x, next= None, random= None):
        self.val = int(x)
        self.next = next
        self.random = random

class ComplexNode(object):
    def __init__(self, value, next=None, sibling=None):
        self.val = value
        self.next = next
        self.sibling = sibling

class Solution:
    def clone_complex_link(self, head):
        # 1.在每一个节点后面克隆一个一样的节点（不带sibling）。
        # 2.设置克隆节点的每一个sibling。
        # 3.创造一个新的头，链接所有偶数节点。
        if not head:return False
        s = p2 = p1 = head
        while head:
            new = ComplexNode(0)
            new.val = head.val+'2'  #加一个2，便于调试
            new.next = head.next
            head.next = new
            if head.next:
                head = head.next.next
            else:
                break
        self.printlinklist(s)

        while p1!=head:
            p1.next.sibling = p1.sibling
            if p1.next.next:
                p1 = p1.next.next
            else:
                break
        
        #偶数的下一个节点是奇数的下一个节点
        cloneList = clonep = p2.next
        p2.next = clonep.next           #连接1，3节点
        p2 = p2.next                    #走到第3节点
        while p2:
            clonep.next = p2.next       #连接2，4节点  2的下一个基点是第3节点的next
            clonep = clonep.next        #偶数走一步
            p2.next = clonep.next       #连接偶节点，3，5
            p2 = p2.next                #奇数走一步

        self.printlinklist(s)
        return cloneList


    def printlinklist(self, head):
        re = []
        while head:
            randomval = head.sibling.val if head.sibling else None
            re.append((head.val,randomval))
            head = head.next
        print(re)

    # 算法：深度优先搜索
    # 从头结点 head 开始拷贝；
    # 由于一个结点可能被多个指针指到，因此如果该结点已被拷贝，则不需要重复拷贝；
    # 如果还没拷贝该结点，则创建一个新的结点进行拷贝，并将拷贝过的结点保存在哈希表中；
    # 使用递归拷贝所有的 next 结点，再递归拷贝所有的 random 结点。
    # 作者：z1m
    # 链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/solution/lian-biao-de-shen-kao-bei-by-z1m/
    def copyRandomList(self, head):
        m = {}
        def dfs(head):
            if not head:return None
            if head in m:return m[head]
            new = ComplexNode(head.val)
            new.next = dfs(head.next)
            new.sibling = dfs(head.sibling)
            return new

        return dfs(head)


        
    
    
# node5 = ComplexNode('E')
# node4 = ComplexNode('D', next=node5)
# node3 = ComplexNode('C', next=node4)
# node2 = ComplexNode('B', next=node3)
# node1 = ComplexNode('A', next=node2)
# node1.sibling = node3
# node2.sibling = node5
# node4.sibling = node2
# head = node1



obj = Solution()
# obj.printlinklist(head)
# re = obj.clone_complex_link(head)
# obj.printlinklist(re)



node5 = ComplexNode('5')
node4 = ComplexNode('4', next=node5)
node3 = ComplexNode('3', next=node4)
node2 = ComplexNode('2', next=node3)
node1 = ComplexNode('1', next=node2)
node1.random = node3
node2.random = node5
node4.random = node2
head = node1
obj.printlinklist(head)
re = obj.copyRandomList(head)
obj.printlinklist(re)


