#!/usr/bin/python
#coding:utf-8

# 面试题 02.02. 返回倒数第 k 个节点
# 实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。

# 注意：本题相对原题稍作改动

# 示例：

# 输入： 1->2->3->4->5 和 k = 2
# 输出： 4
# 说明：

# 给定的 k 保证是有效的。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



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

    def kthToLast(self, head: ListNode, k: int) -> int:
        if not head:return 0 
        s = f = head
        for _ in range(k-1):
            f = f.next
        while f:
            f = f.next
            if not f:return s.val
            s = s.next




nums = [1,2,3,4,5]
o = Solution()
head = o.initlinklist(nums)
h = o.kthToLast(head, 2)
print(h)
# o.printlinklist(head)