# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题04.03.特定深度节点链表
# 
# https://leetcode-cn.com/problems/list-of-depth-lcci/
# 
# 给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。
# &nbsp;
# 
# 示例：
# 
# 输入：[1,2,3,4,5,null,7,8]
# 
#         1
#        /  \ 
#       2    3
#      / \    \ 
#     4   5    7
#    /
#   8
# 
# 输出：[[1],[2,3],[4,5,7],[8]]
# 
# 
# 
# Medium 80.2%
# Testcase Example: [1,2,3,4,5,null,7,8]
# 
# 提示:
# 尝试修改图形搜索算法，从根开始追踪深度。
# 从层号映射到该层节点的散列表或数组也许有些用处。
# 你应该能够提出一个既包括深度优先搜索又包含广度优先搜索的算法。
# 
# 
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
        
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        re = []
        stack = [tree]
        while stack:
            dummy = ListNode(0)
            cur = dummy
            for i in range(len(stack)):
                node = stack.pop(0)
                cur.next = ListNode(node.val)
                cur = cur.next
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            re.append(dummy.next)
        return re

#   1
#  2  3
# 4 5
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)

root = t1
root.left = t2
root.right = t3
t2.left = t4
t2.right = t5
o = Solution()
r = o.listOfDepth(t1)
for i in r:
    o.printlinklist(i)
