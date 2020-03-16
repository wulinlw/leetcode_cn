#
# @lc app=leetcode.cn id=1019 lang=python3
#
# [1019] 链表中的下一个更大节点
#
# https://leetcode-cn.com/problems/next-greater-node-in-linked-list/description/
#
# algorithms
# Medium (51.11%)
# Likes:    54
# Dislikes: 0
# Total Accepted:    5.9K
# Total Submissions: 11.4K
# Testcase Example:  '[2,1,5]'
#
# 给出一个以头节点 head 作为第一个节点的链表。链表中的节点分别编号为：node_1, node_2, node_3, ... 。
# 
# 每个节点都可能有下一个更大值（next larger value）：对于 node_i，如果其 next_larger(node_i) 是
# node_j.val，那么就有 j > i 且  node_j.val > node_i.val，而 j 是可能的选项中最小的那个。如果不存在这样的
# j，那么下一个更大值为 0 。
# 
# 返回整数答案数组 answer，其中 answer[i] = next_larger(node_{i+1}) 。
# 
# 注意：在下面的示例中，诸如 [2,1,5] 这样的输入（不是输出）是链表的序列化表示，其头节点的值为 2，第二个节点值为 1，第三个节点值为 5
# 。
# 
# 
# 
# 示例 1：
# 
# 输入：[2,1,5]
# 输出：[5,5,0]
# 
# 
# 示例 2：
# 
# 输入：[2,7,4,3,5]
# 输出：[7,0,5,5,0]
# 
# 
# 示例 3：
# 
# 输入：[1,7,5,1,9,2,5,1]
# 输出：[7,9,9,9,0,5,0,0]
# 
# 
# 
# 
# 提示：
# 
# 
# 对于链表中的每个节点，1 <= node.val <= 10^9
# 给定列表的长度在 [0, 10000] 范围内
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

    # O(n^2)
    def nextLargerNodes2(self, head: ListNode) -> List[int]:
        if not head:return [0]
        re = []
        cur = head
        while cur:
            p = cur.next if cur.next else None
            nextval = 0
            while p:
                if p.val>cur.val:
                    nextval = p.val
                    break
                else:
                    p = p.next
            re.append(nextval)
            cur = cur.next
        return re

    # 单调栈
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:return [0]
        re = []
        stack = []
        stackIndex = []
        index = -1 
        while head:
            index += 1
            re.append(0)                        #先设为0，不存在默认0
            while stack and stack[-1]<head.val: #找到一个大的了，可以把之前遍历的都处理掉
                re[stackIndex[-1]] = head.val
                stack.pop()
                stackIndex.pop()
            stack.append(head.val)
            stackIndex.append(index)
            head = head.next
        return re
        
# @lc code=end

nums = [2,1,5]
nums = [2,7,4,3,5]
nums = [1,7,5,1,9,2,5,1]
o = Solution()
head = o.initlinklist(nums)
# o.printlinklist(head1)

h = o.nextLargerNodes(head)
print(h)
# o.printlinklist(h)