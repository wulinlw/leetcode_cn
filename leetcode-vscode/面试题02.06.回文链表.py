#!/usr/bin/python
#coding:utf-8

# 面试题 02.06. 回文链表
# 编写一个函数，检查输入的链表是否是回文的。

# 示例 1：
# 输入： 1->2
# 输出： false 

# 示例 2：
# 输入： 1->2->2->1
# 输出： true 
 
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
# https://leetcode-cn.com/problems/palindrome-linked-list-lcci/


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

    def isPalindrome(self, head: ListNode) -> bool:
        if not head:return True
        if not head.next:return True
        def reverseList(head):
            new = None
            while head:
                tmp = head.next
                head.next = new 
                new = head 
                head = tmp 
            return new

        s = f = head
        while f and f.next:
            s = s.next
            if f.next.next:
                f = f.next.next
            else:
                break
        print(s.val,f.val)
        new = reverseList(s)
        self.printlinklist(new)
        s.next = None
        while head and new:
            if head.val!=new.val:
                return False
            if not head or not new:
                return False
            head = head.next 
            new = new.next
        return True



nums = [1, 2]
nums = [1, 2, 2, 1]
# nums = [1, 2, 3,4,5,6]
nums = [1, 0,0]
nums = [1]
# nums = []
o = Solution()
head = o.initlinklist(nums)
o.printlinklist(head)

h = o.isPalindrome(head)
print(h)
# o.printlinklist(h)




