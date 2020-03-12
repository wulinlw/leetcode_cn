#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#
# https://leetcode-cn.com/problems/middle-of-the-linked-list/description/
#
# algorithms
# Easy (64.92%)
# Likes:    156
# Dislikes: 0
# Total Accepted:    29.6K
# Total Submissions: 45.4K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
# 
# 如果有两个中间结点，则返回第二个中间结点。
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,3,4,5]
# 输出：此列表中的结点 3 (序列化形式：[3,4,5])
# 返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
# 注意，我们返回了一个 ListNode 类型的对象 ans，这样：
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next =
# NULL.
# 
# 
# 示例 2：
# 
# 输入：[1,2,3,4,5,6]
# 输出：此列表中的结点 4 (序列化形式：[4,5,6])
# 由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
# 
# 
# 
# 
# 提示：
# 
# 
# 给定链表的结点数介于 1 和 100 之间。
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

    def middleNode(self, head: ListNode) -> ListNode:
        if not head:return None
        s = f = head 
        length = 1
        while f.next:
            length += 1
            f = f.next
        mid = length//2
        while mid>0:
            mid -= 1
            s = s.next
        return s

        
# @lc code=end

nums = [1,2,3,4,5]
# nums = [1,2,3,4,5,6]
o = Solution()
head = o.initlinklist(nums)
o.printlinklist(head)
h = o.middleNode(head)
o.printlinklist(h)