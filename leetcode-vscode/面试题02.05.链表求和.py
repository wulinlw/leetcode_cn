# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题02.05.链表求和
# 
# https://leetcode-cn.com/problems/sum-lists-lcci/
# 
# 给定两个用链表表示的整数，每个节点包含一个数位。
# 这些数位是反向存放的，也就是个位排在链表首部。
# 编写函数对这两个整数求和，并用链表形式返回结果。
# 
# &nbsp;
# 
# 示例：
# 
# 
# 输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
# 输出：2 -> 1 -> 9，即912
# 
# 
# 进阶：假设这些数位是正向存放的，请再做一遍。
# 
# 示例：
# 
# 
# 输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
# 输出：9 -> 1 -> 2，即912
# 
# 
# 
# Medium 45.6%
# Testcase Example: [2,4,3]
# [5,6,4]
# 
# 提示:
# 当然，你可以将链表转换为整数，计算总和，然后将其转换回新的链表。如果你在面试中这样做，面试官可能会接受答案，然后看看你在不能将其转换为数字然后返回的情况下，还能否做到这一点。
# 尝试递归。假设你有两个链表，A = 1 -> 5 -> 9（代表951）和B = 2 -> 3 -> 6 -> 7（代表7632），以及一个操作链表其余部分的函数（5 -> 9和3 -> 6 -> 7）。你能用这个来创建求和方法吗？sum(1 -> 5 -> 9, 2 -> 3 -> 6 -> 7)和sum(5 -> 9, 3 -> 6 -> 7)之间有何关系？
# 确保你考虑到了链表的长度不同的情况。
# 你的算法在形如9 -> 7 -> 8和6 -> 8 -> 5的链表上工作吗？仔细检查一下。
# 对于后续问题：问题是，当链表的长度不一样时，一个链表的首部可能代表1000的位置，而另一个链表代表10的位置。如果你把它们做的一样长呢？有没有方法修改链表来做到这一点，而不改变它所代表的值？
# 
# 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        carry = 0
        while l1 or l2:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            val = l1val + l2val + carry
            carry = val // 10
            p.next = ListNode(val % 10)
            p = p.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            p.next = ListNode(1)
        return dummy.next

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

o = Solution()
l1 = o.initlinklist([7,1,6])
l2 = o.initlinklist([5,9,2])
r = o.addTwoNumbers(l1, l2)
o.printlinklist(r)