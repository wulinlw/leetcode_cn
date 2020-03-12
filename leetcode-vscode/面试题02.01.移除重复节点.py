#!/usr/bin/python
#coding:utf-8

# 面试题 02.01. 移除重复节点
# 编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

# 示例1:

#  输入：[1, 2, 3, 3, 2, 1]
#  输出：[1, 2, 3]
# 示例2:

#  输入：[1, 1, 1, 1, 2]
#  输出：[1, 2]
# 提示：

# 链表长度在[0, 20000]范围内。
# 链表元素在[0, 20000]范围内。
# 进阶：

# 如果不得使用临时缓冲区，该怎么解决？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-duplicate-node-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

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

    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:return None
        m = {}
        f = head
        pre = None
        while f:
            if f.val in m:
                pre.next = f.next
                f = f.next 
                if not f:return head
            else:
                m[f.val] = 1
                pre = f
                f = f.next
        return head


nums = [1, 2, 3, 3, 2, 1]
nums = [1, 1, 1, 1, 2]
o = Solution()
head = o.initlinklist(nums)
o.printlinklist(head)

h = o.removeDuplicateNodes(head)
o.printlinklist(h)