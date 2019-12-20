#!/usr/bin/python
#coding:utf-8

# // 面试题55（一）：二叉树的深度
# // 题目：输入一棵二叉树的根结点，求该树的深度。从根结点到叶结点依次经过的
# // 结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def TreeDepth(self, root):
        if not root :return 0       #结束的时候是0
        return 1+max(self.TreeDepth(root.left), self.TreeDepth(root.right))

        
# 测试树
#        6
#    2     8
#  1  4   7 9                
t1 = TreeNode(1)
t2 = TreeNode(2)
t4 = TreeNode(4)
t6 = TreeNode(6)
t7 = TreeNode(7)
t8 = TreeNode(8)
t9 = TreeNode(9)

root = t6
root.left = t2
root.right = t8
t2.left = t1
t2.right = t4
t8.left = t7
t8.right = t9

obj = Solution()
print(obj.TreeDepth(root))