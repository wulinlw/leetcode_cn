#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (49.23%)
# Likes:    314
# Dislikes: 0
# Total Accepted:    38.3K
# Total Submissions: 77.5K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
# 
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
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

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        successor = None
        def reverseN(head, n):
            nonlocal successor
            if n==1: 
                # 记录第 n + 1 个节点
                successor = head.next
                return head
            last = reverseN(head.next, n-1)
            head.next.next = head
            head.next = successor
            return last
            
        if m==1: 
            return reverseN(head, n)
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head


# @lc code=end

nums = [1,2,3,4,5]
m = 2
n = 4
o = Solution()
head = o.initlinklist(nums)
o.printlinklist(head)

h = o.reverseBetween(head, m, n)
o.printlinklist(h)