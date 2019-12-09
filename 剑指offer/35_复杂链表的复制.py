#!/usr/bin/python
#coding:utf-8

# // 面试题35：复杂链表的复制
# // 题目：请实现函数ComplexListNode* Clone(ComplexListNode* pHead)，复
# // 制一个复杂链表。在复杂链表中，每个结点除了有一个m_pNext指针指向下一个
# // 结点外，还有一个m_pSibling 指向链表中的任意结点或者nullptr。


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
        p2.next = clonep.next
        p2 = p2.next
        while p2:
            clonep.next = p2.next
            clonep = clonep.next
            p2.next = clonep.next
            p2 = p2.next
        return cloneList


    def printlinklist(self, head):
        re = []
        while head:
            re.append(head.val)
            head = head.next
        print(re)
    
    
node5 = ComplexNode('E')
node4 = ComplexNode('D', next=node5)
node3 = ComplexNode('C', next=node4)
node2 = ComplexNode('B', next=node3)
node1 = ComplexNode('A', next=node2)
node1.sibling = node3
node2.sibling = node5
node4.sibling = node2
head = node1



obj = Solution()
obj.printlinklist(head)
re = obj.clone_complex_link(head)
obj.printlinklist(re)




