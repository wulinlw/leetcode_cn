#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (49.22%)
# Likes:    269
# Dislikes: 0
# Total Accepted:    80.1K
# Total Submissions: 162.1K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# 
# 示例 1:
# 
# 输入: 1->1->2
# 输出: 1->2
# 
# 
# 示例 2:
# 
# 输入: 1->1->2->3->3
# 输出: 1->2->3
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
        new.next = s = head
        f = s.next
        while f:
            while s.val==f.val:
                if f.next:
                    f = f.next 
                else:
                    break
            if s.val==f.val:
                s.next=None
                return new.next
            s.next = f 
            s = s.next
            f = f.next
        return new.next

# @lc code=end
nums = [1,2,2,3,3,3,4,5]
nums = [1,1,2,3,3]
o = Solution()
head = o.initlinklist(nums)
o.printlinklist(head)
h = o.deleteDuplicates(head)
o.printlinklist(h)
