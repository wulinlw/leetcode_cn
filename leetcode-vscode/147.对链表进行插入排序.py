#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#
# https://leetcode-cn.com/problems/insertion-sort-list/description/
#
# algorithms
# Medium (63.00%)
# Likes:    136
# Dislikes: 0
# Total Accepted:    22.6K
# Total Submissions: 35.7K
# Testcase Example:  '[4,2,1,3]'
#
# 对链表进行插入排序。
# 
# 
# 插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
# 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。
# 
# 
# 
# 插入排序算法：
# 
# 
# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
# 
# 
# 
# 
# 示例 1：
# 
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 
# 
# 示例 2：
# 
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
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

    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:return None
        dummy = ListNode('-inf')
        dummy.next = head
        cur, nxt = head, head.next
        while nxt:
            if nxt.val>cur.val:
                cur = cur.next
                nxt = nxt.next
            else:
                cur.next = nxt.next 
                p1, p2 = dummy, dummy.next
                while nxt.val > p2.val:
                    p1 = p2
                    p2 = p2.next
                p1.next = nxt       #p1->nxt->p2
                nxt.next = p2
                nxt = cur.next
        return dummy.next

    # 4,2,1,3
    # p1 p2
    # 4  2  1 3       
    # 4 1 3         cur.next = nxt.next
    # 2             p1.next = nxt
    # 2 4 1 3       nxt.next = p2


# @lc code=end

nums = [4,2,1,3]
o = Solution()
head = o.initlinklist(nums)
o.printlinklist(head)

h = o.insertionSortList(head)
o.printlinklist(h)