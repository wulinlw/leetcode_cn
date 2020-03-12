#
# @lc app=leetcode.cn id=1290 lang=python3
#
# [1290] 二进制链表转整数
#
# https://leetcode-cn.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/
#
# algorithms
# Easy (81.16%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    11.9K
# Total Submissions: 14.6K
# Testcase Example:  '[1,0,1]'
#
# 给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。
# 
# 请你返回该链表所表示数字的 十进制值 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：head = [1,0,1]
# 输出：5
# 解释：二进制数 (101) 转化为十进制数 (5)
# 
# 
# 示例 2：
# 
# 输入：head = [0]
# 输出：0
# 
# 
# 示例 3：
# 
# 输入：head = [1]
# 输出：1
# 
# 
# 示例 4：
# 
# 输入：head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
# 输出：18880
# 
# 
# 示例 5：
# 
# 输入：head = [0,0]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 链表不为空。
# 链表的结点总数不超过 30。
# 每个结点的值不是 0 就是 1。
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

    def getDecimalValue(self, head: ListNode) -> int:
        if not head:return None
        re = 0
        while head:
            re = re<<1 | head.val 
            # print("{:0>32b}".format(re))
            head = head.next
            if not head:break
        return re
        
# @lc code=end

nums = [1,0,1]
nums = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
o = Solution()
head = o.initlinklist(nums)
o.printlinklist(head)

h = o.getDecimalValue(head)
print(h)
