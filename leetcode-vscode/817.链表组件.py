#
# @lc app=leetcode.cn id=817 lang=python3
#
# [817] 链表组件
#
# https://leetcode-cn.com/problems/linked-list-components/description/
#
# algorithms
# Medium (55.78%)
# Likes:    31
# Dislikes: 0
# Total Accepted:    5.1K
# Total Submissions: 9K
# Testcase Example:  '[0,1,2,3]\n[0,1,3]'
#
# 给定一个链表（链表结点包含一个整型值）的头结点 head。
# 
# 同时给定列表 G，该列表是上述链表中整型值的一个子集。
# 
# 返回列表 G 中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表 G 中）构成的集合。
# 
# 示例 1：
# 
# 
# 输入: 
# head: 0->1->2->3
# G = [0, 1, 3]
# 输出: 2
# 解释: 
# 链表中,0 和 1 是相连接的，且 G 中不包含 2，所以 [0, 1] 是 G 的一个组件，同理 [3] 也是一个组件，故返回 2。
# 
# 示例 2：
# 
# 
# 输入: 
# head: 0->1->2->3->4
# G = [0, 3, 1, 4]
# 输出: 2
# 解释: 
# 链表中，0 和 1 是相连接的，3 和 4 是相连接的，所以 [0, 1] 和 [3, 4] 是两个组件，故返回 2。
# 
# 注意:
# 
# 
# 如果 N 是给定链表 head 的长度，1 <= N <= 10000。
# 链表中每个结点的值所在范围为 [0, N - 1]。
# 1 <= G.length <= 10000
# G 是链表中所有结点的值的一个子集.
# 
# 
#
from typing import List
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

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        # 当前节点在G中，下一个节点不在，组件+1
        gset = set(G)
        re = 0 
        cur = head
        while cur:
            nxtval = cur.next.val if cur.next else None     #可能没有下一个节点，需要判断
            if cur.val in gset and nxtval not in gset:
                re += 1
            cur = cur.next
        return re
        
# @lc code=end

nums = [0,1,2,3,4]
g = [0,3,1,4]
o = Solution()
head = o.initlinklist(nums)
# o.printlinklist(head1)

h = o.numComponents(head, g)
print(h)
# o.printlinklist(h)