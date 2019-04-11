#!/usr/bin/python
#coding:utf-8

# 两数相加
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)#生成一个链表头，返回的时候返回这个节点
        temp = ans

        tempsum = 0#某一位的总和
        while True:
            if (l1 != None):
                tempsum = l1.val + tempsum
                l1 = l1.next
            if (l2 != None):
                tempsum = l2.val + tempsum
                l2 = l2.next

            temp.val = tempsum % 10     #取和的值，不要进位的1，存入节点，下一行这个值变为进位的值，0或1，1就是有进位，在下一位计算时加上即可
            tempsum  = int(tempsum / 10)#取进位的1

            if l1 == None  and l2 == None and tempsum == 0:
                break

            temp.next = ListNode(0)#生成新节点
            temp = temp.next
        return ans

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

    #反转链表，测试
    # https://www.cnblogs.com/tianqizhi/p/9673894.html
    def ReverseList(self, pHead):
        if pHead is None:
            return pHead
        last = None  #指向上一个节点
        while pHead:
            tmp = pHead.next# 将链表保存到tmp中，后面循环实际是循环这个tmp
            pHead.next = last#在last前面增加节点
            last = pHead#增加完后复制给last，迭代的时候不断往last前增加节点
            pHead = tmp
        return last


s = Solution()
# 有序链表
head1 = s.createListnode([1,5,3])#351
head2 = s.createListnode([2,6,2])#262  #结果613 ，输出316
s.dump(head1)
s.dump(head2)
res = s.addTwoNumbers(head1,head2)
s.dump(res)
r = s.ReverseList(head1)
s.dump(r)
















