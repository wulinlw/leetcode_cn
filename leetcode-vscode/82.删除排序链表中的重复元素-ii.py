#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (46.11%)
# Likes:    229
# Dislikes: 0
# Total Accepted:    36K
# Total Submissions: 77.4K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
# 
# 示例 1:
# 
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 
# 
# 示例 2:
# 
# 输入: 1->1->1->2->3
# 输出: 2->3
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

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:return None
        new = ListNode(0)
        new.next = head
        s = new     #第0位
        f = head    #第1位
        while f:
            if f.next and f.val == f.next.val:          #当前与下一个相等，一直往后走
                while f.next and f.val == f.next.val:
                    f = f.next
                s.next = f.next                         #刚好跳过所有重复的节点
                f = f.next
            else:
                s = s.next                              #不相等的，都往后走一步
                f = f.next
        return new.next

# @lc code=end

nums = [1,2,3,3,4,4,5]
o = Solution()
head = o.initlinklist(nums)
o.printlinklist(head)
h = o.deleteDuplicates(head)
o.printlinklist(h)