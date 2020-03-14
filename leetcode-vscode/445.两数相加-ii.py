#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#
# https://leetcode-cn.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (54.36%)
# Likes:    128
# Dislikes: 0
# Total Accepted:    15.3K
# Total Submissions: 28K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# 给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。
# 
# 
# 
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# 
# 进阶:
# 
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
# 
# 示例:
# 
# 
# 输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出: 7 -> 8 -> 0 -> 7
# 
# 
#

# @lc code=start
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

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 循环计算每一位的和
        # cnt是l1-l2的长度差异
        def dfsCarry(l1, l2, cnt):
            if not l1 or not l2:return 0 
            if cnt>0:
                cursum = l1.val + dfsCarry(l1.next, l2, cnt-1)              #l1往后走，cnt==0时就与l2对齐了，可以计算和与进位
                l1.val = cursum % 10
                return cursum//10
            else:
                cursum = l1.val + l2.val + dfsCarry(l1.next, l2.next, 0)    #长度一样时，每一位的和是l1+l2+carry
                l1.val = cursum % 10
                return cursum//10                                           #进位情况
        
        #计算 l1 l2 的长度
        len1 = len2 = 0
        cur = l1
        while cur:
            len1 += 1
            cur = cur.next
        cur = l2
        while cur:
            len2 += 1
            cur = cur.next
        
        #换下位置 l1是较长的，l2是较短的
        if len2 > len1:
            l1, l2 = l2, l1
            len2, len1 = len1, len2
        
        # 最高位是1的情况，需要进位
        leftsum = dfsCarry(l1, l2, len1-len2)
        if leftsum:
            dummy = ListNode(1)        #进位最前面加节点1即可
            dummy.next = l1
            l1 = dummy                 #更新l1
        return l1
            
    #另外有双栈法，各自压栈，然后计算和，并生成新链表
# @lc code=end

nums1 = [7,2,4,3]
nums2 = [5,6,4,1]
o = Solution()
head1 = o.initlinklist(nums1)
head2 = o.initlinklist(nums2)
# o.printlinklist(head1)

h = o.addTwoNumbers(head1, head2)
# print(h)
o.printlinklist(h)