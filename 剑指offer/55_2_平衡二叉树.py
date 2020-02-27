#!/usr/bin/python
#coding:utf-8

# // 面试题55（二）：平衡二叉树
# // 题目：输入一棵二叉树的根结点，判断该树是不是平衡二叉树。如果某二叉树中
# // 任意结点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 归并的套路，先拿到子结果的集，在处理资结果的集
    def IsBalanced(self, root):
        if not root :return True, 0       #结束的时候是0
        left, left_depth = self.IsBalanced(root.left)
        right, right_depth = self.IsBalanced(root.right)
        if left and right:
            depth = left_depth - right_depth
            if 1>=depth and depth>=-1:                  #高度不超过1
                depth = 1+max(left_depth,right_depth)
                return True,depth
        return False,None

        
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
print(obj.IsBalanced(root))